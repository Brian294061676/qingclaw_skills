# OpenClaw × 轻流 50 Skills 框架设计（v2）

> **核心理念**：以 OpenClaw 的 AI Agent 能力 + 轻流 10.0「搭·问·析·生·联」五大 AI 能力矩阵 + QingClaw MCP 能力，覆盖企业 10 大业务领域，形成"AI 生成 + 无代码搭建 + 数据驱动 + 流程自动化"的完整智能闭环。

---

## 一、轻流 MCP 包与安装基础

### 轻流 MCP 三件套

| 包名 | 用途 | 安装命令 |
|------|------|---------|
| @qingflow-tech/qingflow-cli | CLI命令行工具，支持搭建、发布、调试 | `npm install @qingflow-tech/qingflow-cli@beta` |
| @qingflow-tech/qingflow-app-user-mcp | 运行态能力（数据读写/任务/分析/导入导出） | `npm install @qingflow-tech/qingflow-app-user-mcp@beta` |
| @qingflow-tech/qingflow-app-builder-mcp | 搭建态能力（建模/流程/视图/图表/门户） | `npm install @qingflow-tech/qingflow-app-builder-mcp@beta` |

### 轻流 10.0 五大 AI 能力对照

| 能力维度 | 含义 | 具体能力 |
|---------|------|---------|
| 搭 | AI搭建 | 自然语言建表单应用、自定义页面、AI生成字段结构 |
| 问 | 智能问答 | 小Q智能助手、产品问答、联网搜索、企业知识库RAG |
| 析 | 智能分析 | AI公式生成、AI代码块、AI数据分析、业务洞察 |
| 生 | 内容生成 | AI按钮/节点（文本总结、内容生成、提取、分类、翻译、图片识别/生成、文档解析） |
| 联 | 联动集成 | 表单↔页面联动、QLinker外部API、Q-Robot自动化、MCP跨系统 |

---

## 二、分类体系

### 主轴：10 大业务领域 × 每领域 5 个 = 50 Skills

| 序号 | 领域 | Skills 数量 |
|------|------|-----------|
| 一 | 人力资源 | 5 |
| 二 | 财务管理 | 5 |
| 三 | 运营管理 | 5 |
| 四 | 销售管理 | 5 |
| 五 | 市场营销 | 5 |
| 六 | 技术研发 | 5 |
| 七 | 产品管理 | 5 |
| 八 | 法务合规 | 5 |
| 九 | 项目管理 | 5 |
| 十 | 行政与IT | 5 |
| **合计** | | **50** |

### 副轴：轻流能力维度标签

每个 Skill 标注其核心调用的轻流能力，方便按平台能力维度检索：

| 标签 | 对应轻流能力 | 涉及 MCP 工具 |
|------|-----------|-------------|
| 🏗️ 搭（Builder建模） | AI搭建表单/应用/页面 | app_schema_apply, app_layout_apply, app_flow_apply, app_views_apply, app_charts_apply, portal_apply |
| 📊 析（数据分析） | 数据读取/分析/洞察 | record_list, record_get, record_analyze, chart_get |
| 📝 生（内容生成） | AI生成文案/报告/方案 | AI按钮、AI节点能力，可将结果通过 record_insert 回写 |
| ⚡ 联（流程联动） | 流程自动化/任务执行/外部集成 | task_action_execute, record_code_block_run, q_linker, Q-Robot |
| 👥 问（组织知识） | 人员目录/知识库/智能问答 | directory_search, member_search, 小Q智能助手 |
| 📦 导入导出 | 批量数据处理 | record_import_*, file_upload_local |

---

## 三、50 个 Skills 总览

---

### 一、人力资源（HR）— 5 个 Skills

| # | Skill 名称 | 中文名 | 核心功能 | 轻流能力标签 | 安装命令 |
|---|-----------|--------|---------|-----------|---------|
| 01 | AI Recruiting Engine | 智能招聘引擎 | 简历解析→JD匹配→面试题生成→候选人评估→人才库入库 | 📝📊⚡ | `clawhub install ai-recruiting-engine` |
| 02 | IDA: Instructional Design Agent | 培训设计师 | 培训需求诊断→大纲生成→讲义制作→测试题→考核评估 | 📝 | `clawhub install ida` |
| 03 | Personio | 绩效管理助手 | 目标拆解(KPI/OKR)→进度跟踪→达成差距分析→面谈提纲→改进建议 | 📝📊 | `clawhub install personio` |
| 04 | Onboarding Flow Builder | 入职流程搭建器 | 一键搭建入职审批应用（材料收集→审批→任务清单→试用期跟踪） | 🏗️⚡👥 | `clawhub install onboarding-flow-builder` |
| 05 | HR Analytics Dashboard | 人力数据看板 | 搭建人力分析看板（人员结构/流失率/招聘漏斗/培训完成率） | 🏗️📊 | `clawhub install hr-analytics-dashboard` |

**Skill 间协作链路**：
```
01 招聘引擎(筛选录用) → 04 入职搭建器(入职流转) → 02 培训设计师(岗前培训) → 03 绩效助手(试用期考核) → 05 人力看板(数据沉淀)
```

**轻流深度结合**：
- Skill 01 参考 QingClaw「智能简历识别入库方案」，通过 MCP 自动将候选人信息写入轻流人才库
- Skill 04 通过 `app_schema_apply` + `app_flow_apply` 一键搭建包含多审批节点的入职应用
- Skill 05 通过 `app_charts_apply` + `portal_apply` 搭建 HR 数据门户

**需要的轻流 MCP 包**：
- @qingflow-tech/qingflow-app-user-mcp（Skill 01/02/03 的数据读写与分析）
- @qingflow-tech/qingflow-app-builder-mcp（Skill 04/05 的应用搭建）

---

### 二、财务管理（Finance）— 5 个 Skills

| # | Skill 名称 | 中文名 | 核心功能 | 轻流能力标签 | 安装命令 |
|---|-----------|--------|---------|-----------|---------|
| 06 | Clawshier | 报销审核助手 | 报销单解析→票据校验→制度比对→异常识别→审核意见生成 | 📝📊 | `clawhub install clawshier` |
| 07 | Accounting | 财务分析师 | 多表归集→差异分析→指标诊断→风险预警→分析报告 | 📝📊 | `clawhub install accounting` |
| 08 | Xero | 应收应付管理 | 账款汇总→账期管理→异常核查→催款话术→对账跟进 | 📝📊 | `clawhub install xero` |
| 09 | Budget Planner | 预算编制助手 | 预算模板搭建→历史数据对比→部门预算审批流程→执行偏差预警 | 📝📊🏗️⚡ | `clawhub install budget-planner` |
| 10 | Invoice Processor | 发票处理中心 | 发票OCR识别→进销项匹配→税率校验→台账管理→自动入库 | 📊📦⚡ | `clawhub install invoice-processor` |

**Skill 间协作链路**：
```
10 发票处理(票据入库) → 06 报销审核(费用审核) → 09 预算助手(预算控制) → 07 财务分析(月度分析) → 08 应收应付(账款管理)
```

**轻流深度结合**：
- Skill 09 通过 Builder 搭建完整预算管理应用（部门申报→财务审核→执行跟踪→偏差预警）
- Skill 10 通过 `file_upload_local` 上传发票图片，结合 AI 图片识别能力自动解析，再通过 `record_insert` 写入发票台账
- Skill 06 通过 `task_action_execute` 实现审批流程中的自动审核意见填写

**需要的轻流 MCP 包**：
- @qingflow-tech/qingflow-app-user-mcp（全部5个Skill的数据操作）
- @qingflow-tech/qingflow-app-builder-mcp（Skill 09 的预算应用搭建）

---

### 三、运营管理（Operations）— 5 个 Skills

| # | Skill 名称 | 中文名 | 核心功能 | 轻流能力标签 | 安装命令 |
|---|-----------|--------|---------|-----------|---------|
| 11 | Data Analysis | 运营数据分析师 | 核心指标归集→波动识别→原因拆解→影响分析→复盘结论 | 📝📊 | `clawhub install data-analysis` |
| 12 | CopyWriter | 活动方案生成器 | 活动策划→文案输出→物料清单→执行流程→复盘框架 | 📝 | `clawhub install copywriter` |
| 13 | Review Summarizer | 用户反馈分析师 | 反馈归集→问题分类→情绪判断→优先级排序→优化建议 | 📝📊 | `clawhub install review-summarizer` |
| 14 | Automation Workflows | 运营SOP生成器 | 流程拆解→节点说明→SOP模板→检查清单→风险标记 | 📝🏗️⚡ | `clawhub install automation-workflows` |
| 15 | KPI Dashboard Builder | 运营看板搭建器 | 在轻流中搭建数据看板（图表配置/门户展示/定时刷新） | 🏗️📊 | `clawhub install kpi-dashboard-builder` |

**Skill 间协作链路**：
```
11 数据分析(发现问题) → 13 反馈分析(用户视角) → 12 活动方案(策略执行) → 14 SOP生成(流程固化) → 15 看板搭建(持续监控)
```

**轻流深度结合**：
- Skill 15 参考 QingClaw「应用数据分析方案」，通过 `app_charts_apply` + `portal_apply` 搭建可视化运营门户
- Skill 14 可将 SOP 直接通过 `app_flow_apply` 落地为轻流审批/自动化流程
- Skill 11 通过 `record_analyze` 实现跨表数据分析，支持自然语言查询

**需要的轻流 MCP 包**：
- @qingflow-tech/qingflow-app-user-mcp（Skill 11/13 的数据分析）
- @qingflow-tech/qingflow-app-builder-mcp（Skill 14/15 的应用与看板搭建）

---

### 四、销售管理（Sales）— 5 个 Skills

| # | Skill 名称 | 中文名 | 核心功能 | 轻流能力标签 | 安装命令 |
|---|-----------|--------|---------|-----------|---------|
| 16 | AI Lead Generator | 销售线索挖掘 | 线索整理→意向筛选→分层分类→触达话术→跟进表 | 📝📊 | `clawhub install ai-lead-generator` |
| 17 | Sales Pipeline Tracker | 客户跟进管理 | 跟进记录整理→阶段判断→异议提炼→话术生成→跟进清单 | 📝📊 | `clawhub install sales-pipeline-tracker` |
| 18 | Proposal Writer | 销售方案生成 | 需求提炼→方案框架→能力匹配→话术要点→方案摘要 | 📝 | `clawhub install proposal-writer` |
| 19 | CRM App Builder | 客户管理系统搭建器 | 一键搭建完整CRM（客户表/商机表/跟进记录/合同/销售漏斗看板） | 🏗️📊⚡👥 | `clawhub install crm-app-builder` |
| 20 | Win-Loss Analyzer | 赢输单分析师 | 成交/丢单原因归纳→竞品对比→策略建议→经验沉淀 | 📝📊 | `clawhub install win-loss-analyzer` |

**Skill 间协作链路**：
```
16 线索挖掘(获取线索) → 19 CRM搭建(系统承载) → 17 跟进管理(推进商机) → 18 方案生成(输出方案) → 20 赢输分析(复盘沉淀)
```

**轻流深度结合**：
- Skill 19 是**重量级 Builder Skill**，通过轻流 AI 搭建能力一句话创建 CRM 系统：
  - `app_schema_apply`：定义客户信息、商机、跟进记录等表单字段
  - `app_views_apply`：配置看板视图（按销售阶段分列）
  - `app_flow_apply`：配置合同审批流程
  - `app_charts_apply`：搭建销售漏斗和业绩图表
- Skill 16/17 可通过 `record_insert`/`record_update` 将线索和跟进数据直接写入轻流 CRM

**需要的轻流 MCP 包**：
- @qingflow-tech/qingflow-app-user-mcp（全部5个Skill）
- @qingflow-tech/qingflow-app-builder-mcp（Skill 19 的CRM搭建）

---

### 五、市场营销（Marketing）— 5 个 Skills

| # | Skill 名称 | 中文名 | 核心功能 | 轻流能力标签 | 安装命令 |
|---|-----------|--------|---------|-----------|---------|
| 21 | Marketing Skills | 营销内容生成器 | 选题策划→文案输出→卖点提炼→渠道适配→发布建议 | 📝 | `clawhub install marketing-skills` |
| 22 | Social Media Content Calendar | 社媒内容日历 | 活动方案→宣传文案→排期编排→物料清单→复盘框架 | 📝🏗️ | `clawhub install social-media-content-calendar` |
| 23 | Competitive Intelligence | 市场调研分析师 | 竞品归集→差异提炼→用户需求洞察→机会点→调研结论 | 📝📊 | `clawhub install competitive-intelligence` |
| 24 | SEO Content Optimizer | SEO内容优化师 | 关键词分析→标题优化→内容结构→元数据建议→排名策略 | 📝 | `clawhub install seo-content-optimizer` |
| 25 | Campaign ROI Analyzer | 活动ROI分析师 | 投放数据归集→ROI计算→渠道效果对比→预算优化→策略建议 | 📝📊🏗️ | `clawhub install campaign-roi-analyzer` |

**Skill 间协作链路**：
```
23 市场调研(洞察方向) → 21 内容生成(产出内容) → 24 SEO优化(搜索优化) → 22 内容日历(排期执行) → 25 ROI分析(效果复盘)
```

**轻流深度结合**：
- Skill 22 可通过 Builder 搭建「内容排期管理应用」，配置选题→撰写→审核→发布的协作流程
- Skill 25 通过 `record_analyze` 分析投放数据，`app_charts_apply` 搭建 ROI 分析看板
- 利用轻流 AI 按钮能力，在内容管理表单中一键调用「内容生成」「内容分类」等 AI 节点

**需要的轻流 MCP 包**：
- @qingflow-tech/qingflow-app-user-mcp（Skill 23/25 的数据分析）
- @qingflow-tech/qingflow-app-builder-mcp（Skill 22/25 的应用与看板搭建）

---

### 六、技术研发（Engineering）— 5 个 Skills

| # | Skill 名称 | 中文名 | 核心功能 | 轻流能力标签 | 安装命令 |
|---|-----------|--------|---------|-----------|---------|
| 26 | Technical Documentation Engine | 技术文档生成器 | README结构→项目简介→接口文档→部署手册→技术文档初稿 | 📝 | `clawhub install technical-documentation-engine` |
| 27 | Code Review | 代码评审助手 | Bug识别→规范检查→性能分析→修改建议→评审结论 | 📝 | `clawhub install code-review` |
| 28 | Test Case Generator | 测试用例生成器 | 场景提取→用例设计→异常补充→模板输出→可执行用例表 | 📝 | `clawhub install test-case-generator` |
| 29 | Bug Tracker Flow | 缺陷管理流程搭建器 | 搭建Bug管理应用（提交→分派→修复→验证→关闭），含优先级规则 | 🏗️📊⚡👥 | `clawhub install bug-tracker-flow` |
| 30 | API Integration Builder | API集成搭建器 | 在轻流中配置QLinker外部API对接、代码块逻辑、Webhook触发 | 🏗️⚡🔗 | `clawhub install api-integration-builder` |

**Skill 间协作链路**：
```
26 技术文档(需求理解) → 27 代码评审(质量把关) → 28 测试用例(测试覆盖) → 29 缺陷管理(问题跟踪) → 30 API集成(系统打通)
```

**轻流深度结合**：
- Skill 29 通过 Builder 搭建完整缺陷管理系统，支持 `app_flow_apply` 配置自动分派规则（按模块/优先级路由）
- Skill 30 深度利用轻流的 QLinker 和代码块一体化配置能力：
  - 一次性声明入参字段、代码内容、返回 alias 和目标字段绑定
  - 支持 `record_code_block_run` 运行代码块并自动回写
- 利用轻流「段落布局」能力，让 Bug 表单支持多段落、一行多列的专业布局

**需要的轻流 MCP 包**：
- @qingflow-tech/qingflow-app-builder-mcp（Skill 29/30 的应用搭建与代码块配置）
- @qingflow-tech/qingflow-app-user-mcp（Skill 29 的缺陷数据读写）
- @qingflow-tech/qingflow-cli（Skill 30 的 CLI builder 能力：layout apply、views apply 等）

---

### 七、产品管理（Product）— 5 个 Skills

| # | Skill 名称 | 中文名 | 核心功能 | 轻流能力标签 | 安装命令 |
|---|-----------|--------|---------|-----------|---------|
| 31 | Product Manager | 产品经理助手 | 需求分析→PRD文档框架→功能说明→验收标准→路线图建议 | 📝 | `clawhub install product-manager` |
| 32 | Pricing Strategy | 定价策略师 | 成本分析→定价建模→竞品对比→分层方案→收益优化 | 📝📊 | `clawhub install pricing-strategy` |
| 33 | User Story Writer | 用户故事编写器 | 角色分析→故事编写→验收条件→优先级排序→迭代规划 | 📝 | `clawhub install user-story-writer` |
| 34 | Requirement Pool Builder | 需求池搭建器 | 搭建需求管理应用（需求提交→评审→排期→开发→验收），含优先级视图 | 🏗️📊⚡👥 | `clawhub install requirement-pool-builder` |
| 35 | User Feedback Tracker | 用户反馈跟踪器 | 搭建反馈收集应用（渠道归集→分类标签→关联需求→处理跟踪） | 🏗️📊⚡ | `clawhub install user-feedback-tracker` |

**Skill 间协作链路**：
```
35 反馈跟踪(收集需求) → 31 产品经理(分析输出) → 33 用户故事(拆解故事) → 34 需求池搭建(系统管理) → 32 定价策略(商业决策)
```

**轻流深度结合**：
- Skill 34 通过 Builder 搭建需求池，`app_views_apply` 配置看板视图（按迭代/优先级/状态分组）
- Skill 35 搭建反馈收集门户，通过 `portal_apply` 发布供外部用户提交反馈
- 利用轻流 AI 按钮「内容分类」能力，自动对反馈进行分类标签

**需要的轻流 MCP 包**：
- @qingflow-tech/qingflow-app-builder-mcp（Skill 34/35 的应用搭建）
- @qingflow-tech/qingflow-app-user-mcp（数据读写与分析）

---

### 八、法务合规（Legal）— 5 个 Skills

| # | Skill 名称 | 中文名 | 核心功能 | 轻流能力标签 | 安装命令 |
|---|-----------|--------|---------|-----------|---------|
| 36 | Lawyer | 合同审查助手 | 条款提取→风险识别→版本比对→修改建议→审查意见 | 📝 | `clawhub install lawyer` |
| 37 | Legal Doc Writer | 法务函件生成 | 事实提炼→函件起草→措辞规范→权利主张→回复要求 | 📝 | `clawhub install legal-doc-writer` |
| 38 | Compliance Checker | 合规检查助手 | 制度比对→风险扫描→整改建议→合规报告→定期审查 | 📝📊 | `clawhub install compliance-checker` |
| 39 | Contract Lifecycle Manager | 合同全生命周期管理 | 搭建合同管理应用（起草→审批→签署→履行→到期提醒→归档） | 🏗️📊⚡📦 | `clawhub install contract-lifecycle-manager` |
| 40 | Legal Knowledge Base | 法务知识库搭建器 | 搭建企业法务知识库（法规库/案例库/模板库），支持智能检索 | 🏗️👥 | `clawhub install legal-knowledge-base` |

**Skill 间协作链路**：
```
40 知识库(制度沉淀) → 38 合规检查(风险排查) → 36 合同审查(逐条审核) → 37 函件生成(外部沟通) → 39 合同管理(全程跟踪)
```

**轻流深度结合**：
- Skill 39 搭建合同全生命周期管理系统，含多级审批、到期自动提醒（Q-Robot）
- Skill 40 对接轻流企业知识库 + RAG 能力，支持小Q助手的法务知识问答
- 合同审批流程通过 `app_flow_apply` 配置法务→业务→总经理多级审批

**需要的轻流 MCP 包**：
- @qingflow-tech/qingflow-app-builder-mcp（Skill 39/40 的应用搭建）
- @qingflow-tech/qingflow-app-user-mcp（数据操作与分析）

---

### 九、项目管理（Project Management）— 5 个 Skills

| # | Skill 名称 | 中文名 | 核心功能 | 轻流能力标签 | 安装命令 |
|---|-----------|--------|---------|-----------|---------|
| 41 | Project Board Builder | 项目看板搭建器 | 搭建项目管理应用（任务分派/进度跟踪/甘特图/里程碑管理） | 🏗️📊⚡👥 | `clawhub install project-board-builder` |
| 42 | Meeting Minutes Generator | 会议纪要生成器 | 议题提取→决议整理→待办分派→跟踪提醒→归档沉淀 | 📝📊⚡ | `clawhub install meeting-minutes-generator` |
| 43 | Risk Alert Monitor | 项目风险预警器 | 风险识别→影响评估→预警规则→应对方案→风险台账 | 📝📊🏗️ | `clawhub install risk-alert-monitor` |
| 44 | Timesheet Tracker | 工时统计管理 | 搭建工时填报应用（日报/周报提交→项目工时汇总→人效分析） | 🏗️📊⚡ | `clawhub install timesheet-tracker` |
| 45 | Deliverable Reviewer | 交付物评审助手 | 交付标准梳理→质量检查→评审意见→改进跟踪→验收报告 | 📝📊 | `clawhub install deliverable-reviewer` |

**Skill 间协作链路**：
```
41 项目看板(任务管理) → 44 工时统计(资源投入) → 42 会议纪要(过程沟通) → 43 风险预警(风险管控) → 45 交付评审(质量把关)
```

**轻流深度结合**：
- Skill 41 是典型的 Builder Skill，一键搭建项目管理系统，配置看板视图、甘特图视图
- Skill 42 可将会议纪要中的待办项通过 `record_insert` 自动写入任务表，并触发 Q-Robot 通知
- Skill 44 搭建工时填报表单，通过 `record_analyze` 自动汇总项目人天消耗
- 参考 QingClaw「智能派工解决方案」的架构思路

**需要的轻流 MCP 包**：
- @qingflow-tech/qingflow-app-builder-mcp（Skill 41/43/44 的应用搭建）
- @qingflow-tech/qingflow-app-user-mcp（全部5个Skill的数据操作）

---

### 十、行政与IT（Admin & IT）— 5 个 Skills

| # | Skill 名称 | 中文名 | 核心功能 | 轻流能力标签 | 安装命令 |
|---|-----------|--------|---------|-----------|---------|
| 46 | Asset Manager | 资产管理助手 | 搭建资产管理应用（资产台账/领用归还/折旧计算/盘点管理） | 🏗️📊⚡📦 | `clawhub install asset-manager` |
| 47 | IT Helpdesk Flow | IT工单管理 | 搭建IT工单系统（提交→分派→处理→反馈→满意度评价） | 🏗️⚡👥 | `clawhub install it-helpdesk-flow` |
| 48 | Knowledge Base Builder | 企业知识库搭建器 | 搭建知识管理门户（分类体系/文档管理/搜索/权限配置） | 🏗️📊👥 | `clawhub install knowledge-base-builder` |
| 49 | Office Approval Center | 行政审批中心 | 搭建通用审批应用（用车/用章/采购/会议室等多场景审批） | 🏗️⚡👥 | `clawhub install office-approval-center` |
| 50 | Supplier Evaluation | 供应商评估助手 | 供应商信息归集→评分体系→绩效分析→淘汰预警→推荐报告 | 📝📊🏗️ | `clawhub install supplier-evaluation` |

**Skill 间协作链路**：
```
49 审批中心(采购审批) → 50 供应商评估(选择供应商) → 46 资产管理(资产入库) → 47 IT工单(运维支持) → 48 知识库(经验沉淀)
```

**轻流深度结合**：
- Skill 46-49 均为**重度 Builder 类 Skill**，直接在轻流中搭建完整管理系统
- Skill 47 参考 QingClaw「智能派工方案」，通过 AI 自动识别工单类型并路由到对应IT团队
- Skill 48 对接轻流知识库 + RAG 能力，搭建企业级知识搜索门户
- Skill 49 利用轻流「段落布局」能力，让审批表单根据场景（用车/用章/采购）动态展示不同字段

**需要的轻流 MCP 包**：
- @qingflow-tech/qingflow-app-builder-mcp（全部5个Skill的应用搭建）
- @qingflow-tech/qingflow-app-user-mcp（数据操作与分析）
- @qingflow-tech/qingflow-cli（CLI builder 能力辅助搭建）

---

## 四、轻流能力维度统计

| 轻流能力标签 | 覆盖 Skills 数量 | 占比 | 代表 Skills |
|-----------|---------------|------|-----------|
| 📝 生（AI内容生成） | 35 个 | 70% | 几乎所有 Skill 都具备AI生成能力 |
| 📊 析（数据分析） | 32 个 | 64% | Data Analysis, Accounting, Campaign ROI 等 |
| 🏗️ 搭（Builder建模） | 20 个 | 40% | CRM Builder, Project Board, IT Helpdesk 等 |
| ⚡ 联（流程联动） | 19 个 | 38% | Onboarding Flow, Contract Lifecycle, 审批中心等 |
| 👥 问（组织知识） | 10 个 | 20% | Org Structure, Knowledge Base, IT Helpdesk 等 |
| 📦 导入导出 | 3 个 | 6% | Invoice Processor, Asset Manager, Contract Manager |

### Skill 类型分布

| 类型 | 数量 | 说明 |
|------|------|------|
| 纯 AI 生成型 | 22 个 | 以文案/报告/分析生成为主，结果可回写轻流 |
| AI + 数据操作型 | 8 个 | AI生成 + 读写轻流数据 |
| Builder 搭建型 | 14 个 | 直接在轻流中搭建应用/流程/看板 |
| 综合集成型 | 6 个 | 同时涵盖搭建、数据、流程、AI生成 |

---

## 五、每个 Skill 的标准内容结构

### 1. Skill MD 文件（安装到 OpenClaw）

```yaml
---
name: [英文名]
description: [一句话中英文描述]
color: [颜色标识]
emoji: [图标]
vibe: [一句话调性描述]
qingflow_mcp:
  - @qingflow-tech/qingflow-app-user-mcp    # 按需
  - @qingflow-tech/qingflow-app-builder-mcp  # 按需
  - @qingflow-tech/qingflow-cli              # 按需
---

# [Skill中文名] — [英文名]

## 身份定义
- 角色定位
- 性格特征
- 专业背景

## 核心能力
### 能力一：[名称]
- 具体能力描述
- 输入/输出说明

### 能力二：[名称]
...

## 轻流 MCP 集成说明

### 前置条件
1. 安装轻流 MCP 包（指明具体需要哪些包）
2. 完成认证（auth_login 或 auth_use_token）
3. 选择工作区（workspace_select）

### 可调用的 MCP 工具清单
| 工具 | 用途 | 所属包 |
|------|------|--------|
| record_list | 读取业务数据 | app-user-mcp |
| ... | ... | ... |

### 典型操作流程
STEP 1 → STEP 2 → STEP 3 → ...

## 使用指令示例
指令1：[具体指令描述]
指令2：[具体指令描述]

## 输出示例
[展示该 Skill 的典型输出内容]
```

### 2. 安装教程（每个 Skill 包含）

```markdown
## 安装方式

### 方式一：直接安装 MD 文件
将 Skill 的 .md 文件放入 OpenClaw 的 skills 目录：
~/.openclaw/skills/[skill-name].md

### 方式二：命令行安装
clawhub install [skill-name]

### 方式三：连接轻流 MCP（需要操作轻流数据时）

#### Step 1：安装轻流 MCP 包
npm install @qingflow-tech/qingflow-cli@beta
npm install @qingflow-tech/qingflow-app-user-mcp@beta
npm install @qingflow-tech/qingflow-app-builder-mcp@beta

#### Step 2：认证登录
- 方式A：账号密码登录 → auth_login
- 方式B：Token接入 → auth_use_token

#### Step 3：选择工作区
workspace_list → workspace_select

#### Step 4：验证连接
auth_whoami → 确认身份和工作区
```

---

## 六、交付物清单

| 序号 | 交付物 | 格式 | 说明 |
|------|--------|------|------|
| 1 | 50 个 Skill 的 MD 文件 | .md × 50 | 每个 Skill 一个独立文件，可直接安装到 OpenClaw |
| 2 | Skills 总览介绍表格 | .xlsx | 50 个 Skills 的完整对照表（名称/分类/功能/标签/安装命令/MCP包） |
| 3 | Skills 详细介绍文档 | .docx | 每个 Skill 的详细说明文档 |
| 4 | PPT 介绍文档 | .pptx | 参考原 PDF 风格，按领域展示每个 Skill |

---

## 七、与原 PDF 的对照关系

| PDF中的Skill | 本框架对应编号 | 变化说明 |
|-------------|------------|---------|
| AI Recruiting Engine | #01 | 保留，增加轻流MCP入库能力 |
| IDA | #02 | 保留 |
| Personio | #03 | 保留 |
| Clawshier | #06 | 保留 |
| Accounting | #07 | 保留 |
| Xero | #08 | 保留 |
| Data Analysis | #11 | 保留 |
| CopyWriter | #12 | 保留 |
| Review Summarizer | #13 | 保留 |
| Automation Workflows | #14 | 保留，增加轻流流程落地能力 |
| AI Lead Generator | #16 | 保留 |
| Sales Pipeline Tracker | #17 | 保留 |
| Proposal Writer | #18 | 保留 |
| Marketing Skills | #21 | 保留 |
| Social Media Content Calendar | #22 | 保留 |
| Competitive Intelligence & Market Research | #23 | 保留，简化名称 |
| Technical Documentation Engine | #26 | 保留 |
| Code Review | #27 | 保留 |
| Test Case Generator | #28 | 保留 |
| Product Manager | #31 | 保留 |
| Pricing Strategy | #32 | 保留 |
| Lawyer | #36 | 保留 |
| Legal Doc Writer | #37 | 保留 |
| **原 PDF 保留** | **22 个** | 全部保留并增强轻流集成 |
| **新增 Skills** | **28 个** | 新增轻流Builder类和新领域Skills |
