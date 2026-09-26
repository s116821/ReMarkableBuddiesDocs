"""Verify immutable migration evidence or recover a manifest blob to a new file."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = "docs/migration/imported-blobs.zip"


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def verify(root=ROOT):
    """Return errors; never use Git/network/live imported files or extract ZIP paths."""
    errors = []
    try:
        manifest = json.loads((root / "docs/migration/source-provenance.json").read_text(encoding="utf-8"))
        storage = manifest["storage"]
        if manifest["schemaVersion"] != 2 or storage["path"] != ARCHIVE or storage["format"] != "zip-git-blob-v1":
            return ["Unsupported migration evidence format"]
        archive = root / ARCHIVE
        if hashlib.sha256(archive.read_bytes()).hexdigest() != storage["sha256"]:
            return ["Migration archive SHA-256 mismatch"]
        entries = manifest["files"]
        destinations = [item["destination"] for item in entries]
        if len(entries) != 126 or len(set(destinations)) != 126:
            errors.append("Migration inventory must preserve 126 unique source paths")
        wanted = {item["blob"] for item in entries}
        if any(not re.fullmatch(r"[0-9a-f]{40}", item["blob"]) or
               not re.fullmatch(r"[0-9a-f]{40}", item["sourceCommit"]) or
               not item["sourcePath"] for item in entries):
            errors.append("Invalid source commit/path/blob record")
        with zipfile.ZipFile(archive) as bundle:
            names = bundle.namelist()
            if len(names) != len(set(names)) or set(names) != wanted:
                errors.append("Migration archive member inventory mismatch")
            for blob in wanted.intersection(names):
                entry = bundle.getinfo(blob)
                if entry.file_size > 4 * 1024 * 1024:
                    errors.append(f"Oversized migration blob: {blob}")
                elif git_blob(bundle.read(blob)) != blob:
                    errors.append(f"Migration Git blob hash mismatch: {blob}")
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile, RuntimeError) as error:
        errors.append(f"Cannot verify migration evidence: {error}")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("blob", nargs="?", help="Git blob ID from source-provenance.json")
    parser.add_argument("output", nargs="?", type=Path, help="new destination file; never overwritten")
    args = parser.parse_args(argv)
    if bool(args.blob) != bool(args.output):
        parser.error("Supply both BLOB and OUTPUT, or neither to verify only")
    errors = verify()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    try:
        if args.blob:
            with zipfile.ZipFile(ROOT / ARCHIVE) as bundle:
                data = bundle.read(args.blob)
            with args.output.open("xb") as destination:
                destination.write(data)
            print(f"Recovered exact blob {args.blob} to {args.output}")
        else:
            print("126 original source paths verified from immutable blob archive; no Git history required")
        return 0
    except (OSError, KeyError) as error:
        print(f"Recovery stopped: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
