"""Read-only reuse or explicit selective clone; Python 3.11+, Git, no packages."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def git(*args, cwd=None):
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if result.returncode:
        raise ValueError(result.stderr.strip() or "Git command failed")
    return result.stdout.strip()


def identity(url):
    value = url.strip().rstrip("/")
    if value.endswith(".git"):
        value = value[:-4]
    match = re.fullmatch(r"(?:https://github\.com/|git@github\.com:|ssh://git@github\.com/)([^/]+/[^/]+)", value)
    return "github.com/" + match[1].lower() if match else value


def overrides(values, selected):
    result = {}
    for value in values:
        key, sep, val = value.partition("=")
        if not sep or not val or key not in selected or key in result:
            raise ValueError(f"Use one component=value override per selected component: {value}")
        result[key] = val
    return result


def plan(manifest, selected, workspace, paths, urls):
    actions = []
    for name in selected:
        item = manifest[name]
        target = Path(paths.get(name, workspace / item["directory"])).expanduser().resolve()
        url = urls.get(name, item["url"])
        if url.startswith("-") or "\n" in url:
            raise ValueError(f"Invalid URL for {name}")
        if any(target == previous or target in previous.parents or previous in target.parents
               for _, previous, _, _ in actions):
            raise ValueError(f"Selected destinations overlap: {target}")
        if target.exists():
            if not target.is_dir():
                raise ValueError(f"Destination is not a repository directory: {target}")
            try:
                top = Path(git("rev-parse", "--show-toplevel", cwd=target)).resolve()
            except ValueError as error:
                raise ValueError(f"Existing destination is not a Git clone/worktree: {target}") from error
            if top != target:
                raise ValueError(f"Destination is nested inside another repository: {target}")
            remotes = git("remote", cwd=target).splitlines()
            remote_urls = [git("remote", "get-url", remote, cwd=target) for remote in remotes]
            if identity(url) not in [identity(remote) for remote in remote_urls]:
                raise ValueError(f"Unexpected remote at {target}; use --url {name}=YOUR_FORK_URL for an intentional fork")
            actions.append((name, target, url, "reuse"))
        else:
            parent = target.parent
            while not parent.exists():
                parent = parent.parent
            if not parent.is_dir():
                raise ValueError(f"Destination ancestor is not a directory: {parent}")
            try:
                git("rev-parse", "--show-toplevel", cwd=parent)
            except ValueError:
                pass
            else:
                raise ValueError(f"Refusing to clone inside an existing repository: {target}; choose a sibling workspace")
            actions.append((name, target, url, "clone"))
    return actions


def main(argv=None):
    manifest = json.loads((ROOT / "repositories.json").read_text(encoding="utf-8"))["repositories"]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("components", nargs="*", help="rust and/or manager; no selection lists the directory only")
    parser.add_argument("--all", action="store_true", help="select all implementation components")
    parser.add_argument("--workspace", type=Path, default=ROOT.parent, help="sibling clone directory")
    parser.add_argument("--path", action="append", default=[], help="component=existing-clone-or-worktree-path")
    parser.add_argument("--url", action="append", default=[], help="component=fork-or-mirror-clone-url")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.all and args.components:
            raise ValueError("Choose --all or named components, not both")
        selected = list(name for name in manifest if name != "docs") if args.all else list(dict.fromkeys(args.components))
        if any(name not in manifest or name == "docs" for name in selected):
            raise ValueError("Select rust, manager or --all; Docs is the current checkout")
        paths = overrides(args.path, selected)
        urls = overrides(args.url, selected)
        if not selected:
            for name, item in manifest.items():
                print(f"{name}: {item['role']}\n  {item['url']}\n  Setup: {item['setup']}\n  Checks: {'; '.join(item['checks'])}")
            print("No components selected; nothing changed.")
            return 0
        actions = plan(manifest, selected, args.workspace.resolve(), paths, urls)
        for name, target, url, action in actions:
            print(f"{action}: {name} at {target}")
            if action == "clone" and not args.dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                # Git itself refuses a concurrently created nonempty destination.
                git("clone", "--", url, str(target))
            print(f"  Read {target / 'AGENTS.md'}; {manifest[name]['setup']}")
        return 0
    except (ValueError, OSError) as error:
        print(f"Setup stopped: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
