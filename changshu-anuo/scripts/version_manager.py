from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


SNAPSHOT_ITEMS = [
    "SKILL.md",
    "persona.md",
    "cognition.md",
    "runtime.md",
    "meta.json",
    "agents",
    "references",
    "prompts",
    "scripts",
]


def next_version_name(versions_dir: Path) -> str:
    existing = sorted(
        int(path.name[1:]) for path in versions_dir.iterdir() if path.is_dir() and path.name.startswith("v")
    )
    return f"v{(existing[-1] + 1 if existing else 1):03d}"


def copy_item(source: Path, target: Path) -> None:
    if source.is_dir():
        shutil.copytree(source, target, dirs_exist_ok=True)
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def backup(skill_root: Path) -> Path:
    versions_dir = skill_root / "versions"
    versions_dir.mkdir(parents=True, exist_ok=True)
    version_name = next_version_name(versions_dir)
    target_root = versions_dir / version_name
    target_root.mkdir()
    for item in SNAPSHOT_ITEMS:
        source = skill_root / item
        if source.exists():
            copy_item(source, target_root / item)
    return target_root


def restore(skill_root: Path, version_name: str) -> None:
    source_root = skill_root / "versions" / version_name
    if not source_root.exists():
        raise FileNotFoundError(f"Version not found: {version_name}")
    for item in SNAPSHOT_ITEMS:
        source = source_root / item
        if source.exists():
            copy_item(source, skill_root / item)


def list_versions(skill_root: Path) -> list[str]:
    versions_dir = skill_root / "versions"
    if not versions_dir.exists():
        return []
    return sorted(path.name for path in versions_dir.iterdir() if path.is_dir())


def main() -> int:
    parser = argparse.ArgumentParser(description="Manage changshu-anuo skill snapshots.")
    parser.add_argument("command", choices=["backup", "list", "restore"])
    parser.add_argument("--version", help="Version name for restore")
    skill_root = Path(__file__).resolve().parents[1]
    args = parser.parse_args()

    if args.command == "backup":
        target = backup(skill_root)
        print(f"Created snapshot: {target.name}")
        return 0
    if args.command == "list":
        for version_name in list_versions(skill_root):
            print(version_name)
        return 0
    if not args.version:
        print("--version is required for restore", file=sys.stderr)
        return 1
    restore(skill_root, args.version)
    print(f"Restored {args.version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
