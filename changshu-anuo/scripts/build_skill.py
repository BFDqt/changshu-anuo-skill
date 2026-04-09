from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


FRONTMATTER = """---
name: changshu-anuo
description: 复刻常熟阿诺的语感与脑回路，支持中文扮演、阿诺味改写、以及“他会怎么想/怎么说”的拆解。Use when the user asks for 常熟阿诺、阿诺、诺言诺语、阿诺味、阿诺脑回路，或明确要求用 $changshu-anuo 进行角色化回应。
---
"""


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def parse_sample_count(samples_path: Path) -> Counter:
    counter: Counter[str] = Counter()
    section_count = 0
    for raw_line in samples_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("## Sample:"):
            section_count += 1
        if line.startswith("- type:"):
            sample_type = line.split(":", 1)[1].strip()
            counter[sample_type] += 1
    counter["total"] = section_count
    return counter


def count_corrections(text: str) -> int:
    return len(re.findall(r"^- \[场景:", text, flags=re.MULTILINE))


def render_skill(
    runtime_text: str,
    persona_text: str,
    cognition_text: str,
    meta: dict,
) -> str:
    generated_at = meta["updated_at"]
    return (
        FRONTMATTER
        + "\n"
        + "# 常熟阿诺\n\n"
        + f"生成时间: `{generated_at}`\n\n"
        + "以双核方式工作:\n\n"
        + "- `语感核`: 贴近直播原味、重复、口误、反问和情绪推进\n"
        + "- `脑回路核`: 复刻反问防御、左右脑互搏、面子优先、流量优先、关系执念和情绪先行\n\n"
        + "## 使用原则\n\n"
        + "- 仅在显式调用 `$changshu-anuo` 时进入角色\n"
        + "- 扮演、改写、拆解三模式同时支持\n"
        + "- 遇到证据不足时，优先保持角色内不确定，而不是补完事实\n"
        + "- 公共样品和旧 prompt 只作方法或候选，不作核心事实源\n\n"
        + "## Runtime Rules\n\n"
        + runtime_text
        + "\n\n## Persona Rules\n\n"
        + persona_text
        + "\n\n## Cognition Models\n\n"
        + cognition_text
        + "\n\n## References\n\n"
        + "- 按需读取 `references/evidence-cards.md` 查看规范化证据卡\n"
        + "- 按需读取 `references/sources.md` 查看证据分级与引入规则\n"
        + "- 按需读取 `references/source_samples.md` 查看样本库\n"
        + "- 按需读取 `references/evidence-matrix.md` 查看规则追溯\n"
        + "- 按需读取 `references/negative-examples.md` 压制低质量模仿\n"
        + "- 按需读取 `references/benchmark-prompts.md` 进行效果对比\n"
    )


def main() -> int:
    skill_root = Path(__file__).resolve().parents[1]
    persona_path = skill_root / "persona.md"
    cognition_path = skill_root / "cognition.md"
    runtime_path = skill_root / "runtime.md"
    meta_path = skill_root / "meta.json"
    samples_path = skill_root / "references" / "source_samples.md"
    output_path = skill_root / "SKILL.md"

    persona_text = read(persona_path)
    cognition_text = read(cognition_path)
    runtime_text = read(runtime_path)
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    sample_counts = parse_sample_count(samples_path)
    meta["updated_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
    meta["source_counts"] = {
        "observed": sample_counts.get("observed", 0),
        "derived": sample_counts.get("derived", 0),
        "borrowed": sample_counts.get("borrowed", 0),
        "total": sample_counts.get("total", 0),
    }
    meta["correction_counts"] = {
        "persona": count_corrections(persona_text),
        "cognition": count_corrections(cognition_text),
    }

    output_path.write_text(
        render_skill(runtime_text, persona_text, cognition_text, meta) + "\n",
        encoding="utf-8",
    )
    meta_path.write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Built {output_path}")
    print(json.dumps(meta['source_counts'], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
