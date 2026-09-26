"""Check manifest, current guidance links and preserved import provenance."""
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
IMPORT = "dd9d5e189dc0b901e54396e1cd8bc7ea9393ceac"


def check():
    errors = []
    manifest = json.loads((ROOT / "repositories.json").read_text(encoding="utf-8"))
    if manifest.get("schemaVersion") != 1 or set(manifest["repositories"]) != {"docs", "rust", "manager"}:
        errors.append("Manifest needs schema version 1 and exactly docs/rust/manager")
    for name, item in manifest["repositories"].items():
        for key in ("directory", "url", "role", "issues", "pullRequests", "setup", "checks"):
            if not item.get(key):
                errors.append(f"Missing manifest {name}.{key}")
        if name != "docs" and not item.get("releases"):
            errors.append(f"Missing release source: {name}")
    files = [ROOT / p for p in ("README.md", "AGENTS.md", "CONTRIBUTING.md", "openspec/README.md")]
    files += list((ROOT / "docs").rglob("*.md"))
    files += list((ROOT / ".codex").rglob("SKILL.md")) + list((ROOT / ".agents").rglob("SKILL.md"))
    for file in files:
        text = file.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.split("#")[0].strip("<>")
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not (file.parent / target).exists():
                errors.append(f"Broken local link in {file.relative_to(ROOT)}: {target}")
    provenance = json.loads((ROOT / "docs/migration/source-provenance.json").read_text(encoding="utf-8"))
    # One tree read verifies immutable imported blobs even after live changes evolve.
    tree = subprocess.run(["git", "ls-tree", "-r", IMPORT], cwd=ROOT, capture_output=True, text=True)
    if tree.returncode:
        errors.append("Import history unavailable: fetch full Docs history; migration must preserve import commit")
    else:
        blobs = {line.split("\t", 1)[1]: line.split("\t", 1)[0].split()[2] for line in tree.stdout.splitlines()}
        seen = set()
        for entry in provenance["files"]:
            destination = entry["destination"]
            if destination in seen or blobs.get(destination) != entry["blob"]:
                errors.append(f"Invalid preserved blob: {destination}")
            seen.add(destination)
        if len(seen) != 126:
            errors.append("Migration inventory must preserve all 126 imported files")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Manifest, {len(files)} current guidance files and 126 preserved source blobs verified")
    return 0


if __name__ == "__main__":
    sys.exit(check())
