from __future__ import annotations

import sys
from pathlib import Path


FORBIDDEN_TERMS = [
    "knowledge.txt",
    "调研.md",
    "config.md",
    "别人做的一版本不算完善的SKILL.md",
    "原始素材/",
    "..\\原始素材",
]

SCAN_PATHS = [
    "SKILL.md",
    "persona.md",
    "cognition.md",
    "runtime.md",
    "agents/openai.yaml",
    "references",
    "prompts",
]


def iter_files(skill_root: Path):
    for relative in SCAN_PATHS:
        path = skill_root / relative
        if not path.exists():
            continue
        if path.is_dir():
            for file_path in path.rglob("*"):
                if file_path.is_file():
                    yield file_path
        else:
            yield path


def main() -> int:
    skill_root = Path(__file__).resolve().parents[1]
    violations: list[str] = []
    for file_path in iter_files(skill_root):
        text = file_path.read_text(encoding="utf-8")
        for term in FORBIDDEN_TERMS:
            if term in text:
                violations.append(f"{file_path.relative_to(skill_root)} -> {term}")

    if violations:
        for violation in violations:
            print(f"FORBIDDEN: {violation}")
        return 1

    print("No raw source leaks found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
