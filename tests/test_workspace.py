import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("workspace", ROOT / "scripts/workspace.py")
workspace = importlib.util.module_from_spec(spec)
spec.loader.exec_module(workspace)


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        self.git("init", str(self.source))
        self.git("-C", str(self.source), "config", "user.name", "Test")
        self.git("-C", str(self.source), "config", "user.email", "test@example.invalid")
        (self.source / "tracked").write_text("original")
        self.git("-C", str(self.source), "add", ".")
        self.git("-C", str(self.source), "commit", "-m", "initial")
        self.dest = self.root / "workspace"

    def git(self, *args):
        return subprocess.check_output(["git", *args], stderr=subprocess.STDOUT, text=True).strip()

    def run_setup(self, *args):
        return workspace.main([*args, "--workspace", str(self.dest)])

    def test_docs_default_and_dry_run(self):
        self.assertEqual(self.run_setup(), 0)
        self.assertFalse(self.dest.exists())
        self.assertEqual(self.run_setup("rust", "--dry-run"), 0)
        self.assertFalse(self.dest.exists())

    def test_selective_clone_repeat_dirty(self):
        args = ["rust", "--url", f"rust={self.source}"]
        self.assertEqual(self.run_setup(*args), 0)
        clone = self.dest / "ReMarkableBuddies"
        self.assertFalse((self.dest / "RemarkableBuddiesManager").exists())
        (clone / "tracked").write_text("dirty")
        (clone / "untracked").write_text("keep")
        head = self.git("-C", str(clone), "rev-parse", "HEAD")
        status = self.git("-C", str(clone), "status", "--porcelain")
        self.assertEqual(self.run_setup(*args), 0)
        self.assertEqual(self.git("-C", str(clone), "rev-parse", "HEAD"), head)
        self.assertEqual(self.git("-C", str(clone), "status", "--porcelain"), status)
        self.assertEqual((clone / "untracked").read_text(), "keep")

    def test_dirty_linked_worktree_and_upstream_fork(self):
        clone = self.root / "clone"
        self.git("clone", str(self.source), str(clone))
        self.git("-C", str(clone), "remote", "add", "upstream", "https://github.com/s116821/ReMarkableBuddies.git")
        linked = self.root / "linked with spaces"
        self.git("-C", str(clone), "worktree", "add", "-b", "feature", str(linked))
        (linked / "tracked").write_text("dirty worktree")
        before = self.git("-C", str(linked), "status", "--porcelain")
        self.assertEqual(self.run_setup("rust", "--path", f"rust={linked}"), 0)
        self.assertEqual(self.git("-C", str(linked), "branch", "--show-current"), "feature")
        self.assertEqual(self.git("-C", str(linked), "status", "--porcelain"), before)

    def test_preflight_all_prevents_partial_clone(self):
        bad = self.root / "unrelated"
        bad.mkdir()
        (bad / "keep").write_text("keep")
        self.assertEqual(self.run_setup("--all", "--url", f"rust={self.source}", "--path", f"manager={bad}"), 1)
        self.assertFalse(self.dest.exists())
        self.assertEqual((bad / "keep").read_text(), "keep")

    def test_wrong_remote_and_nested_paths(self):
        self.assertEqual(self.run_setup("rust", "--path", f"rust={self.source}"), 1)
        nested = self.source / "child"
        self.assertEqual(self.run_setup("rust", "--path", f"rust={nested}"), 1)
        nested.mkdir()
        self.assertEqual(self.run_setup("rust", "--path", f"rust={nested}"), 1)

    def test_all_overlaps_and_bad_arguments(self):
        self.assertEqual(self.run_setup("--all", "--url", f"rust={self.source}", "--url", f"manager={self.source}"), 0)
        self.assertTrue((self.dest / "RemarkableBuddiesManager/.git").exists())
        self.assertEqual(self.run_setup("--all", "--path", f"rust={self.root / 'same'}", "--path", f"manager={self.root / 'same'}"), 1)
        self.assertEqual(self.run_setup("unknown"), 1)
        self.assertEqual(self.run_setup("rust", "--url", "manager=x"), 1)
        self.assertEqual(self.run_setup("--all", "rust"), 1)


if __name__ == "__main__":
    unittest.main()
