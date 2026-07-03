# QingClaw Skills — 项目介绍与下一步规划

> 最后更新：2026-07-03

---

## 一、项目概述

**QingClaw Skills** 是基于 [QingClaw（小龙虾）](https://qingflow.com/qing-claw/) AI Agent 平台与 [轻流 10.0](https://qingclaw.oalite.com/) 无代码 aPaaS 的企业级 AI Skill 库。项目以纯 Markdown 定义每个 Skill 的身份、能力、Prompt 模板和 MCP 集成方式，做到"一个 `.md` 文件即一个可安装的 AI Agent"。

核心定位：**AI 生成 + 无代码搭建 + 数据驱动 + 流程自动化 = 企业智能闭环**。

### 关键数字

| 指标 | 数据 |
|------|------|
| Skill 总数 | **68** 个 |
| 覆盖领域 | **12** 个企业业务领域 |
| MCP 工具总数 | **70+** 个可调用工具 |
| 轻流能力维度 | **搭 · 问 · 析 · 生 · 联** 五大 AI 矩阵 |

### 12 大业务领域

| 序号 | 领域 | Skill 数量 | 典型场景 |
|------|------|-----------|---------|
| 01 | 人力资源 (HR) | 6 | 招聘、培训、绩效、入职、人力看板、薪酬分析 |
| 02 | 财务管理 (Finance) | 7 | 报销、分析、预算、发票、回款预测、SOX 审计 |
| 03 | 运营管理 (Operations) | 9 | 数据分析、SOP、看板、流程诊断、经营汇报、智能客服、数据质量 |
| 04 | 销售管理 (Sales) | 7 | 线索、CRM、方案、录音分析、客户画像 |
| 05 | 市场营销 (Marketing) | 6 | 内容、社媒、SEO、ROI、AI 搜索诊断 |
| 06 | 技术研发 (Engineering) | 5 | 文档、代码评审、测试、缺陷、API 集成 |
| 07 | 产品管理 (Product) | 5 | PRD、定价、用户故事、需求池、反馈 |
| 08 | 法务合规 (Legal) | 5 | 合同审查、合规、函件、知识库 |
| 09 | 项目管理 (ProjectMgmt) | 5 | 看板、会议纪要、风险、工时、交付 |
| 10 | 行政与 IT (AdminIT) | 5 | 资产、工单、知识库、审批、供应商 |
| 11 | 生产制造 (Manufacturing) | 4 | 智能排产、交付预测、产能优化、质量管控 |
| 12 | 供应链 (SupplyChain) | 4 | 需求预测、履约预测、询价比价、库存优化 |

---

## 二、技术架构

### 2.1 Skill 文件结构

```
skills/
├── 01-HR/                     # 人力资源（6 Skills）
├── 02-Finance/                # 财务管理（7 Skills）
├── 03-Operations/             # 运营管理（9 Skills）
├── 04-Sales/                  # 销售管理（7 Skills）
├── 05-Marketing/              # 市场营销（6 Skills）
├── 06-Engineering/            # 技术研发（5 Skills）
├── 07-Product/                # 产品管理（5 Skills）
├── 08-Legal/                  # 法务合规（5 Skills）
├── 09-ProjectMgmt/            # 项目管理（5 Skills）
├── 10-AdminIT/                # 行政与IT（5 Skills）
├── 11-Manufacturing/          # 生产制造（4 Skills）
└── 12-SupplyChain/            # 供应链（4 Skills）
```

每个 Skill 是一个带 YAML frontmatter 的 Markdown 文件：

```yaml
---
name: AI Recruiting Engine
description: AI招聘引擎——简历解析→JD匹配→面试题生成
color: blue
emoji: 🎯
vibe: 让招聘变成一次智能匹配
qingflow_mcp:
  - @qingflow-tech/qingflow-app-user-mcp
---
```

### 2.2 轻流 MCP 三件套

所有 Skill 已统一迁移至 `@qingflow-tech` 官方包：

| 包名 | 用途 | 安装命令 |
|------|------|---------|
| `@qingflow-tech/qingflow-cli` | CLI（搭建/发布/调试） | `npm install @qingflow-tech/qingflow-cli` |
| `@qingflow-tech/qingflow-app-user-mcp` | 运行态（数据 CRUD / 任务 / 分析 / 导入导出） | `npm install @qingflow-tech/qingflow-app-user-mcp` |
| `@qingflow-tech/qingflow-app-builder-mcp` | 搭建态（建模 / 流程 / 视图 / 图表 / 门户） | `npm install @qingflow-tech/qingflow-app-builder-mcp` |

### 2.3 认证方式

推荐使用 `auth_use_credential` 进行认证，MCP 自动解析 token / wsId / qfVersion 上下文，工作区自动绑定，无需手动 `workspace_select`。

### 2.4 构建流程

```bash
python3 scripts/build_openclaw_local_skills.py
```

该脚本将 `skills/**/*.md` 转换为 QingClaw 安装时所需的 `qingclaw_local_skills/<slug>/SKILL.md` 目录结构。每次运行会删除并重建输出目录。（输出目录已于 2026-07-03 由 `openclaw_local_skills/` 重命名为 `qingclaw_local_skills/`，`.gitignore` 与 `CLAUDE.md` 同步更新。）

### 2.5 五大能力维度覆盖

| 标签 | 能力维度 | 覆盖 Skills | 占比 |
|------|---------|------------|------|
| 📝 生 | AI 内容生成 | 51 | 75% |
| 📊 析 | 智能分析 | 49 | 72% |
| 🏗️ 搭 | AI 搭建 | 22 | 32% |
| ⚡ 联 | 流程联动 | 33 | 49% |
| 👥 问 | 组织知识 | 9 | 13% |
| 📦 导入导出 | 批量数据 | 5 | 7% |

> 占比基于 68 个 Skill 实际标签统计（`rg -l` 逐 emoji 计数）。

---

## 三、项目现状

### 已完成（2026-07-03 全量同步）

- **68 个 Skill MD 文件**全部完成，覆盖 12 个企业领域（含 #63–#68 六个 B3 扩展：智能客服 / 数据质量检测 / SOX 审计 / 库存优化 / 质量管控 / 薪酬分析）
- **B1 质量增强**：62 个原 Skill 统一补充「输入/输出示例」对照表 + 更多使用指令示例
- 所有 Skill 已从 `@josephyan` 迁移至 `@qingflow-tech` 官方 MCP 包
- 认证方式统一为 `auth_use_credential`，去除 `@beta` / `@latest` 后缀和 `-g` 全局安装标记
- 新增工具引用：`record_insert_schema_get`、`record_update_schema_get`、`record_browse_schema_get` 等
- **README.md / CLAUDE.md 已同步至 68 Skills / 12 领域**（A2/A3 完成）
- **构建脚本输出目录重命名** `openclaw_local_skills/` → `qingclaw_local_skills/`，`.gitignore` 与 `CLAUDE.md` 同步（A4 完成）
- 品牌统一：OpenClaw → QingClaw
- **B4 协作链路方案落地**：见 `QingClaw_Skills_协作链路与行业套件.md`（6 条端到端链路 + 数据契约标准 + 4 个行业套件）
- 全部成果已推送到 GitHub `master`（commit `5325293`）

### 已知问题

- 本轮 A1–A4、B1、B3、B4 已全部完成，技术层面的已知问题清零
- 本地二进制素材（PDF/PPTX/DOCX/MOV/PNG/XLSX）与 `agency-agents-main/` 外部参考按 `.gitignore` 策略不纳入仓库

---

## 四、待办事项

### A. 近期技术任务（紧急度：高）— ✅ 全部完成

- ✅ **A1. 推送到 GitHub** — 已推送至 `origin/master`（commit `5325293`）
- ✅ **A2. 更新 README.md** — 已同步至 68 Skills / 12 领域，五大占比重算，品牌 OpenClaw→QingClaw，认证改 `auth_use_credential`
- ✅ **A3. 更新 CLAUDE.md** — 已同步至 62→68、12 领域、编号 01–68，补 Manufacturing/SupplyChain
- ✅ **A4. 更新构建脚本** — 输出目录改名 + `.gitignore` 同步 + 构建验证（生成 68 个产物）

### B. 中期产品规划（1-2 个月）

#### B1. Skill 质量提升 — ✅ 主体完成

- ✅ 为每个 Skill 添加「输入/输出示例」对照表
- ⬜ 统一所有 Skill 的 prompt 模板格式，增强一致性
- ✅ 补充更多使用指令示例

#### B2. 自动化测试与验证 — ⬜ 待启动

- 编写 CI 脚本校验所有 Skill 的 frontmatter 完整性（description 必填、slug 不重复）
- 校验 qingflow_mcp 依赖声明与 Skill 正文中引用的工具是否一致
- 校验 README 表格中的能力标签是否与各 Skill 文件匹配
- 校验协作链路契约 YAML（producer/consumer Skill 是否存在、字段引用是否一致）

#### B3. Skill 扩展计划 — ✅ 首批完成

首批 6 个方向已全部落地：

| 方向 | 已交付 Skill | 编号 |
|------|-----------|------|
| 客户服务 | 智能客服 Agent | #63 |
| 数据工程 | 数据质量检测 Agent | #64 |
| 合规审计 | SOX 审计助手 | #65 |
| 供应链 | 库存优化 Agent | #66 |
| 生产制造 | 质量管控 Agent | #67 |
| HR | 薪酬分析 Agent | #68 |

#### B4. 协作链路强化 — ✅ 方案完成，落地进行中

方案见 `QingClaw_Skills_协作链路与行业套件.md`：6 条端到端链路、数据契约标准、4 个行业套件模板。下一步按其"五、落地路线图"M1→M3 推进。

### C. 长期战略方向（3-6 个月）

#### C1. 解决方案包化

- 按行业/场景打包 Skill 组合为轻流解决方案包（`package_apply` + 关联应用）
- 提供"一键部署"体验：安装一个包即获得 5-8 个 Skill + 预配置应用 + 门户
- 第一批：协作链路文档定义的制造业 / 电商 / 专业服务 / 集团职能四大套件

#### C2. Skill 市场化

- 建立 Skill 评分和使用反馈机制
- 支持社区贡献 Skill（定义 Contribution Guide 和质量标准）
- 接入 QingClaw 的 Skill 分发渠道

#### C3. 多语言支持

- 当前 Skill 正文全部中文，可扩展英文/日文版本以覆盖海外市场
- Frontmatter 保持英文 name，body 增加 `lang` 字段支持多语言切换

#### C4. 智能编排层

- 构建 Skill Orchestrator：根据用户自然语言意图自动选择和编排多个 Skill
- 结合轻流的流程引擎实现 Skill 间的自动触发和数据流转
- 支持 Skill 执行结果的自动评估和反馈闭环

---

## 五、仓库信息

| 项 | 值 |
|----|-----|
| GitHub | [Brian294061676/qingclaw_skills](https://github.com/Brian294061676/qingclaw_skills) |
| 分支 | `master` |
| 在线介绍 | [QingClaw Skills 介绍页](https://qingclawskills.lovable.app) |
| 技术栈 | Markdown + YAML frontmatter + Python 构建脚本 |
| MCP 包管理 | npm (@qingflow-tech) |
| License | MIT |
