#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "skills"
OUTPUT_DIR = ROOT / "openclaw_local_skills"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
NUMBERED_STEM_RE = re.compile(r"^\d+-(.+)$")


def load_skill_file(path: Path) -> tuple[dict, str]:
    content = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(content)
    if not match:
        raise ValueError(f"Missing YAML frontmatter: {path}")
    frontmatter = parse_frontmatter(match.group(1), path)
    body = content[match.end() :].lstrip("\n")
    return frontmatter, body


def parse_frontmatter(frontmatter_text: str, source_path: Path) -> dict:
    parsed: dict[str, object] = {}
    lines = frontmatter_text.splitlines()
    idx = 0

    while idx < len(lines):
        raw_line = lines[idx]
        line = raw_line.rstrip()
        idx += 1

        if not line.strip():
            continue

        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line in {source_path}: {raw_line}")

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not key:
            raise ValueError(f"Invalid frontmatter key in {source_path}: {raw_line}")

        if value:
            parsed[key] = value
            continue

        items: list[str] = []
        while idx < len(lines):
            item_line = lines[idx]
            if not item_line.strip():
                idx += 1
                continue
            if not re.match(r"^\s*-\s+", item_line):
                break
            items.append(re.sub(r"^\s*-\s+", "", item_line).strip())
            idx += 1

        parsed[key] = items

    return parsed


def skill_slug(path: Path) -> str:
    stem = path.stem
    match = NUMBERED_STEM_RE.match(stem)
    slug = match.group(1) if match else stem
    return slug.strip().lower()


def build_frontmatter(source_path: Path, frontmatter: dict, slug: str) -> dict:
    description = str(frontmatter.get("description", "")).strip()
    if not description:
        raise ValueError(f"Missing description: {source_path}")

    legacy_meta = {
        "source_file": source_path.relative_to(ROOT).as_posix(),
        "display_name": str(frontmatter.get("name", slug)).strip(),
    }

    for key in ("color", "emoji", "vibe", "qingflow_mcp"):
        if key in frontmatter:
            legacy_meta[key] = frontmatter[key]

    return {
        "name": slug,
        "description": description,
        "metadata": {
            "legacy": legacy_meta,
        },
    }


def render_skill(frontmatter: dict, body: str) -> str:
    rendered_frontmatter = yaml.safe_dump(
        frontmatter,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ).strip()
    return f"---\n{rendered_frontmatter}\n---\n\n{body.rstrip()}\n"


def main() -> None:
    if not SOURCE_DIR.exists():
        raise SystemExit(f"Source directory not found: {SOURCE_DIR}")

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    seen: set[str] = set()
    generated = 0

    for source_path in sorted(SOURCE_DIR.rglob("*.md")):
        frontmatter, body = load_skill_file(source_path)
        slug = skill_slug(source_path)
        if slug in seen:
            raise SystemExit(f"Duplicate slug detected: {slug}")
        seen.add(slug)

        output_path = OUTPUT_DIR / slug / "SKILL.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_frontmatter = build_frontmatter(source_path, frontmatter, slug)
        output_path.write_text(render_skill(output_frontmatter, body), encoding="utf-8")
        generated += 1

    print(f"Generated {generated} QingClaw-local skills in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
