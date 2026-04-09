from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


REQUIRED_FIELDS = [
    "id",
    "场景",
    "tier",
    "type",
    "来源",
    "摘录",
    "为什么像",
    "脑回路标签",
    "可复用句式",
    "禁改点",
]

VALID_TYPES = {"observed", "derived", "borrowed"}
SECTION_RE = re.compile(r"^## Sample:\s*(.+?)\s*$", re.MULTILINE)
FIELD_RE = re.compile(r"^- ([^:]+):\s*(.*)$")
CARD_ID_RE = re.compile(r"^(OBS|DER|BOR)-\d{3}$")


def parse_sections(text: str) -> list[dict]:
    matches = list(SECTION_RE.finditer(text))
    samples: list[dict] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sample = {"title": match.group(1).strip()}
        for line in body.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            field_match = FIELD_RE.match(line)
            if field_match:
                key = field_match.group(1).strip()
                value = field_match.group(2).strip()
                sample[key] = value
        samples.append(sample)
    return samples


def split_tokens(value: str) -> list[str]:
    if not value:
        return []
    pieces = re.split(r"[，,;/]\s*", value)
    return [piece.strip() for piece in pieces if piece.strip()]


def validate_samples(samples: list[dict]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    seen_ids: set[str] = set()
    reusable_counter: Counter[str] = Counter()

    for sample in samples:
        sample_id = sample.get("id", "<missing>")
        missing = [field for field in REQUIRED_FIELDS if not sample.get(field)]
        if missing:
            errors.append(f"{sample_id}: missing fields {', '.join(missing)}")

        sample_type = sample.get("type")
        if sample_type and sample_type not in VALID_TYPES:
            errors.append(f"{sample_id}: invalid type {sample_type}")

        source_refs = split_tokens(sample.get("来源", ""))
        if not source_refs:
            errors.append(f"{sample_id}: empty 来源")
        for source_ref in source_refs:
            if ".txt" in source_ref or ".md" in source_ref or "原始素材" in source_ref:
                errors.append(f"{sample_id}: raw source leak in 来源 -> {source_ref}")
            elif not CARD_ID_RE.match(source_ref):
                errors.append(f"{sample_id}: invalid 来源 token {source_ref}")

        if sample_id in seen_ids:
            errors.append(f"{sample_id}: duplicate id")
        seen_ids.add(sample_id)

        tags = split_tokens(sample.get("脑回路标签", ""))
        if not tags:
            errors.append(f"{sample_id}: empty 脑回路标签")

        reusable_phrases = split_tokens(sample.get("可复用句式", ""))
        for phrase in reusable_phrases:
            reusable_counter[phrase] += 1

    for phrase, count in reusable_counter.items():
        if count >= 5:
            warnings.append(
                f"phrase '{phrase}' appears {count} times in 可复用句式; check overfitting"
            )

    return errors, warnings


def build_index(samples: list[dict]) -> dict:
    type_counter = Counter()
    tier_counter = Counter()
    scene_counter = Counter()
    tag_counter = Counter()

    normalized_samples = []
    for sample in samples:
        tags = split_tokens(sample.get("脑回路标签", ""))
        phrases = split_tokens(sample.get("可复用句式", ""))
        normalized = dict(sample)
        normalized["脑回路标签"] = tags
        normalized["可复用句式"] = phrases
        normalized_samples.append(normalized)

        if sample.get("type"):
            type_counter[sample["type"]] += 1
        if sample.get("tier"):
            tier_counter[sample["tier"]] += 1
        if sample.get("场景"):
            scene_counter[sample["场景"]] += 1
        for tag in tags:
            tag_counter[tag] += 1

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "samples": normalized_samples,
        "stats": {
            "total": len(samples),
            "by_type": dict(type_counter),
            "by_tier": dict(tier_counter),
            "by_scene": dict(scene_counter),
            "top_tags": tag_counter.most_common(20),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize changshu-anuo sample library.")
    skill_root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--samples",
        type=Path,
        default=skill_root / "references" / "source_samples.md",
        help="Path to source_samples.md",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=skill_root / "references" / "source_samples.index.json",
        help="Output JSON index path",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with non-zero code on validation errors",
    )
    args = parser.parse_args()

    text = args.samples.read_text(encoding="utf-8")
    samples = parse_sections(text)
    errors, warnings = validate_samples(samples)
    index = build_index(samples)

    args.output.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Samples: {len(samples)}")
    print(f"Output: {args.output}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
