#!/usr/bin/env python3
"""QingClaw Skills 一致性校验（规划 B2）。

零第三方依赖（纯 stdlib），供本地与 GitHub Actions 调用。

校验项：
  A. frontmatter 完整性：description / name 必填，slug 全局唯一，qingflow_mcp 取值合法
  B. MCP 依赖与能力标签一致（遵循 CLAUDE.md 的 taxonomy）：
     - 含 🏗️搭 → 必须声明 qingflow-app-builder-mcp
     - 含 📊析 / ⚡联 / 📦导入导出 → 必须声明 qingflow-app-user-mcp
  C. README 索引一致性：skills/ 下的编号集合 == README 表格里的编号集合

退出码：发现任何 error 则 1，否则 0。warning 不影响退出码。

用法：python .github/scripts/check_skills.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # .github/scripts/ → 仓库根
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"

BUILDER_EMOJI = "🏗️"
DATA_EMOJI = ("📊", "⚡", "📦")
VALID_MCP = {
    "@qingflow-tech/qingflow-cli",
    "@qingflow-tech/qingflow-app-user-mcp",
    "@qingflow-tech/qingflow-app-builder-mcp",
}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)
NUMBERED_STEM_RE = re.compile(r"^(\d+)-(.+)$")
README_NUMBER_RE = re.compile(r"^\|\s*(\d{2})\s*\|")


def parse_frontmatter(text: str) -> tuple[dict | None, str]:
    """解析 YAML frontmatter（轻量手写，与构建脚本同逻辑，避免引入 pyyaml）。"""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, text
    parsed: dict = {}
    lines = match.group(1).splitlines()
    idx = 0
    while idx < len(lines):
        line = lines[idx].rstrip()
        idx += 1
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value:
            parsed[key] = value
            continue
        items: list[str] = []
        while idx < len(lines) and re.match(r"^\s*-\s+", lines[idx]):
            items.append(re.sub(r"^\s*-\s+", "", lines[idx]).strip())
            idx += 1
        parsed[key] = items
    return parsed, text[match.end():]


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"❌ skills/ 目录不存在：{SKILLS_DIR}", file=sys.stderr)
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    slug_seen: dict[str, str] = {}
    skill_numbers: dict[int, str] = {}

    for path in sorted(SKILLS_DIR.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(text)

        if frontmatter is None:
            errors.append(f"{rel}: 缺少 frontmatter")
            continue

        numbered = NUMBERED_STEM_RE.match(path.stem)
        number = int(numbered.group(1)) if numbered else None
        slug = (numbered.group(2) if numbered else path.stem).strip().lower()

        # A. frontmatter 完整性
        if not str(frontmatter.get("description", "")).strip():
            errors.append(f"{rel}: description 必填且不能为空")
        if not str(frontmatter.get("name", "")).strip():
            errors.append(f"{rel}: name 必填")
        if slug in slug_seen:
            errors.append(f"{rel}: slug 重复「{slug}」（已见于 {slug_seen[slug]}）")
        else:
            slug_seen[slug] = rel

        mcps = frontmatter.get("qingflow_mcp", [])
        if isinstance(mcps, str):
            mcps = [mcps] if mcps else []
        for mcp in mcps:
            if mcp not in VALID_MCP:
                errors.append(f"{rel}: 未知的 qingflow_mcp 值「{mcp}」")

        # B. 能力标签 ↔ MCP 依赖
        if BUILDER_EMOJI in body and not any("builder-mcp" in x for x in mcps):
            errors.append(f"{rel}: 含 🏗️搭 标签但未声明 qingflow-app-builder-mcp")
        if any(e in body for e in DATA_EMOJI) and not any("app-user-mcp" in x for x in mcps):
            errors.append(f"{rel}: 含数据类标签（📊/⚡/📦）但未声明 qingflow-app-user-mcp")

        if number is not None:
            if number in skill_numbers:
                errors.append(f"{rel}: 编号 #{number:02d} 重复（已见于 {skill_numbers[number]}）")
            else:
                skill_numbers[number] = rel
        else:
            warnings.append(f"{rel}: 文件名无数字前缀，未计入编号索引")

    # C. README 索引一致性
    readme_numbers: set[int] = set()
    if README.exists():
        for line in README.read_text(encoding="utf-8").splitlines():
            m = README_NUMBER_RE.match(line)
            if m:
                readme_numbers.add(int(m.group(1)))
    else:
        errors.append("README.md 不存在")

    for n in sorted(set(skill_numbers) - readme_numbers):
        errors.append(f"#{n:02d} 在 skills/ 存在但 README 表格缺失")
    for n in sorted(readme_numbers - set(skill_numbers)):
        errors.append(f"#{n:02d} 在 README 表格出现但 skills/ 无对应文件")

    # 汇总
    print(f"校验 {len(skill_numbers)} 个 Skill / README 索引 {len(readme_numbers)} 个编号")
    for w in warnings:
        print(f"  ⚠️  {w}")
    if errors:
        print(f"\n❌ 发现 {len(errors)} 个错误：")
        for e in errors:
            print(f"  ✗ {e}")
        return 1
    print("✅ 全部校验通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
