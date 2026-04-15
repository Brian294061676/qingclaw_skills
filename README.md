# QingClaw Skills — OpenClaw × 轻流 50 Skills

> AI Agent + 无代码平台 · 企业智能化解决方案

以 [QingClaw](https://qingflow.com/qing-claw/)的 AI Agent 能力 + [轻流 10.0](https://qingclaw.oalite.com/)「搭·问·析·生·联」五大 AI 能力矩阵，覆盖企业 **10 大业务领域 × 5 = 50 个 Skills**，形成 "AI 生成 + 无代码搭建 + 数据驱动 + 流程自动化" 的完整智能闭环。

**相关链接**：[QingClaw 客户端下载](https://qingflow.com/qing-claw/) | [轻流官网](https://qingflow.com) | [轻流 10.0 介绍](https://qingclaw.oalite.com/) | [50 Skills 介绍](https://qingclawskills.lovable.app)

---

## 轻流 10.0 五大 AI 能力维度

| 标签 | 能力维度 | 说明 | 覆盖 Skills | 占比 |
|------|---------|------|------------|------|
| 📝 生 | AI 内容生成 | AI 生成文案 / 报告 / 方案 | 35 | 70% |
| 📊 析 | 智能分析 | 数据读取 / 分析 / 洞察 | 32 | 64% |
| 🏗️ 搭 | AI 搭建 | 自然语言建表单 / 应用 / 页面 | 20 | 40% |
| ⚡ 联 | 流程联动 | 流程自动化 / 任务执行 / 外部集成 | 19 | 38% |
| 👥 问 | 组织知识 | 人员目录 / 知识库 / 智能问答 | 10 | 20% |
| 📦 导入导出 | 批量数据 | 批量数据处理 | 3 | 6% |

---

## 轻流 MCP 三件套

| 包名 | 用途 | 安装命令 | 适用类型 |
|------|------|---------|---------|
| `@josephyan/qingflow-cli` | CLI 命令行工具（搭建 / 发布 / 调试） | `npm install @josephyan/qingflow-cli@beta` | Builder 类 Skill 的 CLI 辅助 |
| `@josephyan/qingflow-app-user-mcp` | 运行态能力（数据读写 / 任务 / 分析 / 导入导出） | `npm install @josephyan/qingflow-app-user-mcp@beta` | 所有需要读写轻流数据的 Skill |
| `@josephyan/qingflow-app-builder-mcp` | 搭建态能力（建模 / 流程 / 视图 / 图表 / 门户） | `npm install @josephyan/qingflow-app-builder-mcp@beta` | 所有 Builder 类（🏗️搭）Skill |

### MCP 连接步骤

```bash
# Step 1: 安装轻流 MCP 包
npm install @josephyan/qingflow-cli@beta
npm install @josephyan/qingflow-app-user-mcp@beta
npm install @josephyan/qingflow-app-builder-mcp@beta

# Step 2: 认证登录（二选一）
# 方式A：账号密码登录 → auth_login
# 方式B：Token 接入 → auth_use_token

# Step 3: 选择工作区
# workspace_list → workspace_select

# Step 4: 验证连接
# auth_whoami → 确认身份和工作区
```

---

## Skill 安装方式

将对应的 `.md` 文件直接发送给 OpenClaw（小龙虾）即可安装使用。每个 Skill 均为独立的 Markdown 文件，包含完整的身份定义、能力描述和使用指令。

---

## 50 Skills 总览

### 一、人力资源 (HR)

> 覆盖招聘、培训、绩效、入职、人力分析全流程，AI 赋能 HR 从事务型向战略型转变

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 01 | 智能招聘引擎 (AI Recruiting Engine) | 简历解析→JD匹配→面试题生成→候选人评估→人才库入库 | 📝📊⚡ | app-user-mcp |
| 02 | 培训设计师 (IDA) | 培训需求诊断→大纲生成→讲义制作→测试题→考核评估 | 📝 | - |
| 03 | 绩效管理助手 (Personio) | 目标拆解(KPI/OKR)→进度跟踪→达成差距分析→面谈提纲 | 📝📊 | app-user-mcp |
| 04 | 入职流程搭建器 (Onboarding Flow Builder) | 一键搭建入职审批应用（材料收集→审批→任务清单→试用期跟踪） | 🏗️⚡👥 | app-builder + app-user |
| 05 | 人力数据看板 (HR Analytics Dashboard) | 搭建人力分析看板（人员结构/流失率/招聘漏斗/培训完成率） | 🏗️📊 | app-builder + app-user |

**协作链路**：`01 招聘引擎 → 04 入职搭建器 → 02 培训设计师 → 03 绩效助手 → 05 人力看板`

---

### 二、财务管理 (Finance)

> 覆盖报销、分析、应收应付、预算、发票全场景，AI 让财务从核算型走向分析型

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 06 | 报销审核助手 (Clawshier) | 报销单解析→票据校验→制度比对→异常识别→审核意见生成 | 📝📊 | app-user-mcp |
| 07 | 财务分析师 (Accounting) | 多表归集→差异分析→指标诊断→风险预警→分析报告 | 📝📊 | app-user-mcp |
| 08 | 应收应付管理 (Xero) | 账款汇总→账期管理→异常核查→催款话术→对账跟进 | 📝📊 | app-user-mcp |
| 09 | 预算编制助手 (Budget Planner) | 预算模板搭建→历史对比→审批流程→执行偏差预警→分析报告 | 📝📊🏗️⚡ | app-builder + app-user |
| 10 | 发票处理中心 (Invoice Processor) | 发票OCR识别→进销项匹配→税率校验→台账管理→自动入库 | 📊📦⚡ | app-user-mcp |

**协作链路**：`10 发票处理 → 06 报销审核 → 09 预算助手 → 07 财务分析 → 08 应收应付`

---

### 三、运营管理 (Operations)

> 覆盖数据分析、活动策划、用户反馈、SOP 管理、运营看板全链路

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 11 | 运营数据分析师 (Data Analysis) | 核心指标归集→波动识别→原因拆解→影响分析→复盘结论 | 📝📊 | app-user-mcp |
| 12 | 活动方案生成器 (CopyWriter) | 活动策划→文案输出→物料清单→执行流程→复盘框架 | 📝 | - |
| 13 | 用户反馈分析师 (Review Summarizer) | 反馈归集→问题分类→情绪判断→优先级排序→优化建议 | 📝📊 | app-user-mcp |
| 14 | 运营SOP生成器 (Automation Workflows) | 流程拆解→SOP模板→检查清单→风险标记→轻流流程落地 | 📝🏗️⚡ | app-builder + app-user |
| 15 | 运营看板搭建器 (KPI Dashboard Builder) | 看板设计→图表搭建→门户发布→数据分析→摘要读取 | 🏗️📊 | app-builder + app-user |

**协作链路**：`11 数据分析 → 13 反馈分析 → 12 活动方案 → 14 SOP生成 → 15 看板搭建`

---

### 四、销售管理 (Sales)

> 覆盖线索挖掘、客户跟进、方案生成、CRM 搭建、赢输分析全流程

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 16 | 销售线索挖掘 (AI Lead Generator) | 线索整理→意向筛选→分层分类→触达话术→跟进表 | 📝📊 | app-user-mcp |
| 17 | 客户跟进管理 (Sales Pipeline Tracker) | 跟进记录整理→阶段判断→异议提炼→话术生成→跟进清单 | 📝📊 | app-user-mcp |
| 18 | 销售方案生成 (Proposal Writer) | 需求提炼→方案框架→能力匹配→话术要点→方案摘要 | 📝 | - |
| 19 | 客户管理系统搭建器 (CRM App Builder) | 一键搭建完整CRM（客户/商机/跟进/合同/销售漏斗看板） | 🏗️📊⚡👥 | app-builder + app-user |
| 20 | 赢输单分析师 (Win-Loss Analyzer) | 成交/丢单原因归纳→竞品对比→策略建议→经验沉淀 | 📝📊 | app-user-mcp |

**协作链路**：`16 线索挖掘 → 19 CRM搭建 → 17 跟进管理 → 18 方案生成 → 20 赢输分析`

---

### 五、市场营销 (Marketing)

> 覆盖内容生成、社媒管理、市场调研、SEO 优化、ROI 分析全链路

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 21 | 营销内容生成器 (Marketing Skills) | 选题策划→卖点提炼→多渠道文案→传播话术→发布建议 | 📝 | - |
| 22 | 社媒内容日历 (Social Media Content Calendar) | 活动方案→宣传文案→排期编排→物料清单→轻流搭建 | 📝🏗️ | app-builder |
| 23 | 市场调研分析师 (Competitive Intelligence) | 竞品归集→差异提炼→用户洞察→机会分析→调研结论 | 📝📊 | app-user-mcp |
| 24 | SEO内容优化师 (SEO Content Optimizer) | 关键词分析→标题优化→内容结构→元数据生成→策略建议 | 📝 | - |
| 25 | 活动ROI分析师 (Campaign ROI Analyzer) | 投放数据归集→ROI计算→渠道对比→优化建议→轻流看板 | 📝📊🏗️ | app-builder + app-user |

**协作链路**：`23 市场调研 → 21 内容生成 → 24 SEO优化 → 22 内容日历 → 25 ROI分析`

---

### 六、技术研发 (Engineering)

> 覆盖技术文档、代码评审、测试用例、缺陷管理、API 集成全流程

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 26 | 技术文档生成器 (Technical Documentation Engine) | README→项目简介→架构说明→接口文档→部署手册 | 📝 | - |
| 27 | 代码评审助手 (Code Review) | Bug识别→规范检查→性能分析→修改建议→评审结论 | 📝 | - |
| 28 | 测试用例生成器 (Test Case Generator) | 场景提取→用例设计→异常补充→模板输出→可执行用例表 | 📝 | - |
| 29 | 缺陷管理流程搭建器 (Bug Tracker Flow) | 搭建Bug管理应用（提交→分派→修复→验证→关闭） | 🏗️📊⚡👥 | app-builder + app-user |
| 30 | API集成搭建器 (API Integration Builder) | QLinker配置→代码块配置→代码块执行→Webhook→集成调试 | 🏗️⚡ | app-builder + app-user |

**协作链路**：`26 技术文档 → 27 代码评审 → 28 测试用例 → 29 缺陷管理 → 30 API集成`

---

### 七、产品管理 (Product)

> 覆盖需求分析、定价策略、用户故事、需求池管理、反馈跟踪全流程

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 31 | 产品经理助手 (Product Manager) | 需求分析→PRD框架→功能说明→验收标准→路线图建议 | 📝 | - |
| 32 | 定价策略师 (Pricing Strategy) | 成本分析→定价建模→竞品对比→分层方案→收益优化 | 📝📊 | app-user-mcp |
| 33 | 用户故事编写器 (User Story Writer) | 角色分析→故事编写→验收条件→优先级排序→迭代规划 | 📝 | - |
| 34 | 需求池搭建器 (Requirement Pool Builder) | 需求表单→评审流程→看板视图→数据统计→门户发布 | 🏗️📊⚡👥 | app-builder + app-user |
| 35 | 用户反馈跟踪器 (User Feedback Tracker) | 反馈表单→AI分类标签→关联需求→处理流程→反馈看板 | 🏗️📊⚡ | app-builder + app-user |

**协作链路**：`35 反馈跟踪 → 31 产品经理 → 33 用户故事 → 34 需求池搭建 → 32 定价策略`

---

### 八、法务合规 (Legal)

> 覆盖合同审查、法务函件、合规检查、合同管理、知识库搭建全流程

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 36 | 合同审查助手 (Lawyer) | 条款提取→风险识别→版本比对→修改建议→审查意见 | 📝 | - |
| 37 | 法务函件生成 (Legal Doc Writer) | 事实提炼→函件起草→措辞规范→权利主张→回复要求 | 📝 | - |
| 38 | 合规检查助手 (Compliance Checker) | 制度比对→风险扫描→整改建议→合规报告→审查提醒 | 📝📊 | app-user-mcp |
| 39 | 合同全生命周期管理 (Contract Lifecycle Manager) | 合同表单→多级审批→到期提醒→合同台账→归档管理 | 🏗️📊⚡📦 | app-builder + app-user |
| 40 | 法务知识库搭建器 (Legal Knowledge Base) | 知识分类→知识库搭建→内容导入→智能检索→权限管理 | 🏗️👥 | app-builder + app-user |

**协作链路**：`40 知识库 → 38 合规检查 → 36 合同审查 → 37 函件生成 → 39 合同管理`

---

### 九、项目管理 (ProjectMgmt)

> 覆盖项目看板、会议纪要、风险预警、工时管理、交付评审全流程

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 41 | 项目看板搭建器 (Project Board Builder) | 项目表单→任务流程→看板视图→进度图表→里程碑管理 | 🏗️📊⚡👥 | app-builder + app-user |
| 42 | 会议纪要生成器 (Meeting Minutes Generator) | 议题提取→决议整理→待办分派→跟踪提醒→纪要归档 | 📝📊⚡ | app-user-mcp |
| 43 | 项目风险预警器 (Risk Alert Monitor) | 风险识别→影响评估→预警规则→应对方案→风险台账 | 📝📊🏗️ | app-builder + app-user |
| 44 | 工时统计管理 (Timesheet Tracker) | 工时表单→填报流程→工时汇总→人效分析→提醒机制 | 🏗️📊⚡ | app-builder + app-user |
| 45 | 交付物评审助手 (Deliverable Reviewer) | 标准梳理→质量检查→评审意见→改进跟踪→验收报告 | 📝📊 | app-user-mcp |

**协作链路**：`41 项目看板 → 44 工时统计 → 42 会议纪要 → 43 风险预警 → 45 交付评审`

---

### 十、行政与 IT (AdminIT)

> 覆盖资产管理、IT 工单、知识库、行政审批、供应商评估全场景

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 46 | 资产管理助手 (Asset Manager) | 资产表单→领用归还→折旧计算→盘点管理→资产看板 | 🏗️📊⚡📦 | app-builder + app-user |
| 47 | IT工单管理 (IT Helpdesk Flow) | 工单表单→AI分类→智能分派→处理跟踪→满意度评价 | 🏗️⚡👥 | app-builder + app-user |
| 48 | 企业知识库搭建器 (Knowledge Base Builder) | 分类体系→知识表单→搜索门户→RAG对接→权限配置 | 🏗️📊👥 | app-builder + app-user |
| 49 | 行政审批中心 (Office Approval Center) | 多场景表单→段落布局→审批流程→统一门户→审批统计 | 🏗️⚡👥 | app-builder + app-user |
| 50 | 供应商评估助手 (Supplier Evaluation) | 信息归集→评分体系→绩效分析→淘汰预警→推荐报告 | 📝📊🏗️ | app-builder + app-user |

**协作链路**：`49 审批中心 → 50 供应商评估 → 46 资产管理 → 47 IT工单 → 48 知识库`

---

## 目录结构

```
skills/
├── 01-HR/                  # 人力资源（5 Skills）
├── 02-Finance/             # 财务管理（5 Skills）
├── 03-Operations/          # 运营管理（5 Skills）
├── 04-Sales/               # 销售管理（5 Skills）
├── 05-Marketing/           # 市场营销（5 Skills）
├── 06-Engineering/         # 技术研发（5 Skills）
├── 07-Product/             # 产品管理（5 Skills）
├── 08-Legal/               # 法务合规（5 Skills）
├── 09-ProjectMgmt/         # 项目管理（5 Skills）
└── 10-AdminIT/             # 行政与IT（5 Skills）
```

每个 Skill 以独立 Markdown 文件呈现，包含：身份定义、能力描述、Prompt 模板、轻流能力标签、MCP 依赖、协作链路等完整信息。

---

## License

MIT

---

> **OpenClaw × 轻流 — 让每个企业都拥有智能化的工作方式**
