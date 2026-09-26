import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import warnings
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("provenance", ROOT / "scripts/provenance.py")
provenance = importlib.util.module_from_spec(spec)
spec.loader.exec_module(provenance)


class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        directory = self.root / "docs/migration"
        directory.mkdir(parents=True)
        self.archive = self.root / provenance.ARCHIVE
        self.manifest = directory / "source-provenance.json"
        shutil.copyfile(ROOT / provenance.ARCHIVE, self.archive)
        shutil.copyfile(ROOT / "docs/migration/source-provenance.json", self.manifest)

    def rewrite_archive(self, transform):
        with zipfile.ZipFile(ROOT / provenance.ARCHIVE) as source:
            entries = [(name, source.read(name)) for name in source.namelist()]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(self.archive, "w", compression=zipfile.ZIP_DEFLATED) as target:
                for name, data in transform(entries):
                    target.writestr(name, data)
        manifest = json.loads(self.manifest.read_text())
        manifest["storage"]["sha256"] = hashlib.sha256(self.archive.read_bytes()).hexdigest()
        self.manifest.write_text(json.dumps(manifest))

    def test_no_git_or_live_files_needed(self):
        self.assertFalse((self.root / ".git").exists())
        self.assertFalse((self.root / "openspec").exists())
        self.assertEqual(provenance.verify(self.root), [])
        # Future source edits/deletions do not alter preserved evidence.
        live = self.root / "openspec/README.md"
        live.parent.mkdir()
        live.write_text("completely revised guidance")
        self.assertEqual(provenance.verify(self.root), [])
        live.unlink()
        self.assertEqual(provenance.verify(self.root), [])

    def test_archive_checksum_corruption(self):
        with self.archive.open("ab") as destination:
            destination.write(b"tampered")
        self.assertIn("SHA-256 mismatch", " ".join(provenance.verify(self.root)))

    def test_member_inventory(self):
        for name, transform in (
            ("missing", lambda entries: entries[1:]),
            ("extra", lambda entries: entries + [("unexpected", b"extra")]),
            ("duplicate", lambda entries: entries + [entries[0]]),
        ):
            with self.subTest(name=name):
                self.rewrite_archive(transform)
                self.assertIn("inventory mismatch", " ".join(provenance.verify(self.root)))

    def test_member_hash_even_with_updated_archive_checksum(self):
        self.rewrite_archive(lambda entries: [(entries[0][0], b"changed")] + entries[1:])
        self.assertIn("Git blob hash mismatch", " ".join(provenance.verify(self.root)))

    def test_manifest_blob_and_path_inventory(self):
        manifest = json.loads(self.manifest.read_text())
        manifest["files"][0]["blob"] = "0" * 40
        manifest["files"][0]["destination"] = manifest["files"][1]["destination"]
        self.manifest.write_text(json.dumps(manifest))
        errors = " ".join(provenance.verify(self.root))
        self.assertIn("126 unique source paths", errors)
        self.assertIn("inventory mismatch", errors)

    def test_recovery_exact_bytes_and_no_overwrite(self):
        manifest = json.loads(self.manifest.read_text())
        blob = manifest["files"][0]["blob"]
        output = self.root / "recovered original.md"
        with patch.object(provenance, "ROOT", self.root), patch.object(provenance, "verify", return_value=[]):
            self.assertEqual(provenance.main([blob, str(output)]), 0)
            self.assertEqual(provenance.git_blob(output.read_bytes()), blob)
            self.assertEqual(provenance.main([blob, str(output)]), 1)
            self.assertEqual(provenance.git_blob(output.read_bytes()), blob)
            self.assertEqual(provenance.main(["0" * 40, str(self.root / "unknown")]), 1)
            self.assertFalse((self.root / "unknown").exists())


if __name__ == "__main__":
    unittest.main()
