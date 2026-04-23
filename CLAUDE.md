# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A library of **51 Markdown-defined AI Skills** for the QingClaw / 轻流 10.0 no-code platform, organized across 10 enterprise domains (HR, Finance, Operations, Sales, Marketing, Engineering, Product, Legal, ProjectMgmt, AdminIT). Each Skill is an authored prompt/persona file; there is no runtime application code. The only executable code is a small Python build script that transforms source Skills into the directory layout OpenClaw (小龙虾) expects at install time.

## Build command

```bash
python3 scripts/build_openclaw_local_skills.py
```

This regenerates `openclaw_local_skills/` from `skills/**/*.md`. The script **deletes and recreates** `openclaw_local_skills/` on every run (see `scripts/build_openclaw_local_skills.py:116-118`) — do not hand-edit files under that directory, they will be overwritten. Requires `pyyaml`.

Both `scripts/` and `openclaw_local_skills/` are gitignored; the canonical source of truth is `skills/`.

## Skill authoring model

Two directory layouts coexist and must stay in sync via the build script:

- **`skills/<NN-Domain>/<NN-slug>.md`** — authored source. Domain prefix (`01-HR` … `10-AdminIT`) groups skills; file prefix (`01-` … `51-`) provides the global Skill number referenced in `README.md`'s 51-Skills tables.
- **`openclaw_local_skills/<slug>/SKILL.md`** — generated install-ready output. Slug = source stem with the numeric prefix stripped (`01-ai-recruiting-engine.md` → `ai-recruiting-engine/SKILL.md`).

### Frontmatter contract

Source files use authoring frontmatter:

```yaml
---
name: <Human-readable English name>
description: <One-line Chinese pitch — required>
color: <ui color>
emoji: <single emoji>
vibe: <one-line tagline>
qingflow_mcp:
  - @qingflow-tech/qingflow-app-user-mcp      # or -builder-mcp, or -cli
---
```

The build script (`scripts/build_openclaw_local_skills.py:79-99`) rewrites this into a different shape for the generated `SKILL.md`: top-level `name` becomes the slug, `description` is kept verbatim, and `name`/`color`/`emoji`/`vibe`/`qingflow_mcp` are preserved under `metadata.legacy.*` along with a `source_file` backpointer. `description` is mandatory; the build fails without it. Slugs must be globally unique across all domain directories — duplicate slugs abort the build.

When adding a new Skill:
1. Pick the next global number (currently 51 are used; see README tables for numbering).
2. Place the file under the correct `skills/<NN-Domain>/` directory.
3. Update the corresponding domain table **and** the "协作链路" (collaboration chain) line in `README.md` — these are the human-maintained index.
4. Re-run the build script.

## MCP dependency taxonomy

Each Skill declares which of the three QingClaw MCP packages it requires. These drive what Claude-in-OpenClaw can actually call at runtime:

- `@qingflow-tech/qingflow-cli` — CLI auth / workspace / publish helpers
- `@qingflow-tech/qingflow-app-user-mcp` — runtime data plane (record CRUD, analysis, directory, tasks, import/export, files, code blocks)
- `@qingflow-tech/qingflow-app-builder-mcp` — design-time plane (schema, layout, flow, views, charts, portals, packages, roles)

Skill capability tags (📝生 / 📊析 / 🏗️搭 / ⚡联 / 👥问 / 📦导入导出) should match the declared `qingflow_mcp` deps: any 🏗️搭 Skill needs `-builder-mcp`; data-touching Skills (📊析, ⚡联, 📦) need `-app-user-mcp`; pure 📝生 content Skills may declare no MCP dependency. The full MCP tool catalog is enumerated in `README.md` under "轻流 MCP 能力清单" — treat that section as the authoritative list when a Skill references a specific tool name.

## Conventions

- Skill bodies are authored in **Chinese** (with English skill names kept in titles and frontmatter `name`). Follow existing tone — second-person `你是 ...`, followed by 身份定义 / 核心能力 / sections matching the domain's pattern.
- The `README.md` tables are the canonical Skill index: numbering, capability tags, and MCP deps shown there must match each Skill file's frontmatter and body.
- Do not edit `openclaw_local_skills/` directly. Do not commit it (gitignored).
- `agency-agents-main/` is vendored external reference material, not part of this project's Skill set.
