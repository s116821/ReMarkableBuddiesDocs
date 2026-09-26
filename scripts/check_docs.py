"""Check manifest, current guidance links and preserved import provenance."""
import json
from pathlib import Path
import re
import sys
from provenance import verify

ROOT = Path(__file__).resolve().parents[1]


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
    errors.extend(verify(ROOT))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Manifest, {len(files)} current guidance files and 126 preserved source blobs verified")
    return 0


if __name__ == "__main__":
    sys.exit(check())
