# QingClaw Skills — 轻流 68 Skills

> AI Agent + 无代码平台 · 企业智能化解决方案

以 [QingClaw](https://qingflow.com/qing-claw/) 的 AI Agent 能力 + [轻流 10.0](https://qingclaw.oalite.com/)「搭·问·析·生·联」五大 AI 能力矩阵，覆盖企业 **12 大业务领域 68 个 Skills**，形成 "AI 生成 + 无代码搭建 + 数据驱动 + 流程自动化" 的完整智能闭环。

**相关链接**：[QingClaw 客户端下载](https://qingflow.com/qing-claw/) | [轻流官网](https://qingflow.com) | [轻流 10.0 介绍](https://qingclaw.oalite.com/) | [Skills 介绍](https://qingclawskills.lovable.app)

---

## 轻流 10.0 五大 AI 能力维度

| 标签 | 能力维度 | 说明 | 覆盖 Skills | 占比 |
|------|---------|------|------------|------|
| 📝 生 | AI 内容生成 | AI 生成文案 / 报告 / 方案 | 51 | 75% |
| 📊 析 | 智能分析 | 数据读取 / 分析 / 洞察 | 49 | 72% |
| 🏗️ 搭 | AI 搭建 | 自然语言建表单 / 应用 / 页面 | 24 | 35% |
| ⚡ 联 | 流程联动 | 流程自动化 / 任务执行 / 外部集成 | 33 | 49% |
| 👥 问 | 组织知识 | 人员目录 / 知识库 / 智能问答 | 10 | 15% |
| 📦 导入导出 | 批量数据 | 批量数据处理 | 5 | 7% |

---

## 轻流 MCP 三件套

| 包名 | 用途 | 安装命令 | 适用类型 |
|------|------|---------|---------|
| `@qingflow-tech/qingflow-cli` | CLI 命令行工具（搭建 / 发布 / 调试） | `npm install @qingflow-tech/qingflow-cli` | Builder 类 Skill 的 CLI 辅助 |
| `@qingflow-tech/qingflow-app-user-mcp` | 运行态能力（数据读写 / 任务 / 分析 / 导入导出） | `npm install @qingflow-tech/qingflow-app-user-mcp` | 所有需要读写轻流数据的 Skill |
| `@qingflow-tech/qingflow-app-builder-mcp` | 搭建态能力（建模 / 流程 / 视图 / 图表 / 门户） | `npm install @qingflow-tech/qingflow-app-builder-mcp` | 所有 Builder 类（🏗️搭）Skill |

### MCP 连接步骤

```bash
# Step 1: 安装轻流 MCP 包
npm install @qingflow-tech/qingflow-cli
npm install @qingflow-tech/qingflow-app-user-mcp
npm install @qingflow-tech/qingflow-app-builder-mcp

# Step 2: 凭证接入（推荐 auth_use_credential，自动解析 token / wsId / qfVersion）
# auth_use_credential → 工作区自动绑定，无需手动 workspace_select

# Step 3: 验证连接
# auth_whoami → 确认身份和工作区
```

---

## 15 大 Agent 场景总览

> 以实际业务场景为线索，横跨 12 大领域，展示 15 个核心 Agent 如何解决企业痛点。

### 场景矩阵

| # | Agent 场景 | 适用角色 | 核心输出 | 对应 Skill | 覆盖状态 |
|---|----------|---------|---------|-----------|---------|
| 1 | 🏭 智能排产 | 计划员、生产主管、车间主任 | 排产方案、订单优先级、计划冲突检测 | #52 Smart Production Scheduler | ✅ |
| 2 | 🚚 交付预测 | 生产主管、销售/客服、管理层 | 风险订单、延期原因、调整建议 | #53 Delivery Prediction | ✅ |
| 3 | ⚙️ 产能优化 | 车间主任、班组长、设备负责人 | 瓶颈分析、负荷情况、优化建议 | #54 Capacity Optimization | ✅ |
| 4 | 👤 客户画像 | 销售、销售主管、客服/客成 | 客户画像、需求标签、跟进建议 | #55 Customer Profile | ✅ |
| 5 | 🔄 商机卡点 | 销售、销售主管、售前 | 停滞商机、卡点原因、推进建议 | #17 Sales Pipeline Tracker | ✅ 已覆盖 |
| 6 | 💰 回款预测 | 销售、财务、销售主管 | 回款风险、逾期预测、催收建议 | #56 Collection Forecast | ✅ |
| 7 | 📈 需求预测 | 采购、仓库、供应链负责人 | 需求预测、缺货风险、补货建议 | #57 Demand Forecast | ✅ |
| 8 | 📦 履约预测 | 采购、供应商管理、生产计划 | 履约风险、延期预测、交付影响 | #58 Supplier Fulfillment | ✅ |
| 9 | ⚖️ 询价比价 | 采购、采购主管、财务 | 比价结果、供应商建议、采购依据 | #59 Quotation Comparison | ✅ |
| 10 | 🔎 AI 搜索诊断 | 市场、品牌、增长运营 | 品牌提及、推荐结果、问题诊断 | #60 AI Search Diagnostics | ✅ |
| 11 | ✏️ 内容优化 | 市场、内容运营、SEO/GEO 运营 | 内容建议、FAQ 草稿、优化方案 | #24 SEO Content Optimizer | ✅ 已覆盖 |
| 12 | 🕵️ 竞品监测 | 市场、销售、管理层 | 竞品提及、优势对比、差距分析 | #23 Competitive Intelligence | ✅ 已覆盖 |
| 13 | 📊 数据分析 | 管理层、业务负责人、数据分析 | 指标变化、异常数据、分析结论 | #11 Data Analysis + #15 KPI Dashboard | ✅ 已覆盖 |
| 14 | 🩺 流程诊断 | 管理层、流程负责人、部门主管 | 流程卡点、超时节点、优化建议 | #61 Process Diagnostics | ✅ |
| 15 | 📋 经营汇报 | 管理层、部门负责人、运营人员 | 经营摘要、汇报材料、改进事项 | #62 Business Report | ✅ |

### 场景分组

**制造与供应链**（Agent 1-3, 7-9）：形成"需求预测 → 排产计划 → 产能优化 → 交付跟踪 → 履约管控 → 询价比价"端到端链路。

```
#57 需求预测 → #52 智能排产 → #54 产能优化 → #53 交付预测 → #58 履约预测 → #59 询价比价
```

**销售与回款**（Agent 4-6）：打通"客户建档 → 商机推进 → 回款管控"全周期。

```
#55 客户画像 → #17 商机跟进 → #56 回款预测
```

**市场与增长**（Agent 10-12）：覆盖"竞品洞察 → 内容优化 → AI 搜索布局"三位一体。

```
#23 竞品监测 → #24 内容优化 → #60 AI 搜索诊断
```

**经营管理**（Agent 13-15）：实现"数据看板 → 流程优化 → 经营复盘"管理闭环。

```
#11 数据分析 + #15 看板搭建 → #61 流程诊断 → #62 经营汇报
```

---

## Skill 安装方式

将对应的 `.md` 文件直接发送给 QingClaw（小龙虾）即可安装使用。每个 Skill 均为独立的 Markdown 文件，包含完整的身份定义、能力描述和使用指令。

---

## 68 Skills 总览

### 一、人力资源 (HR)

> 覆盖招聘、培训、绩效、入职、人力分析、薪酬分析全流程，AI 赋能 HR 从事务型向战略型转变

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 01 | 智能招聘引擎 (AI Recruiting Engine) | 简历解析→JD匹配→面试题生成→候选人评估→人才库入库 | 📝📊⚡ | app-user-mcp |
| 02 | 培训设计师 (IDA) | 培训需求诊断→大纲生成→讲义制作→测试题→考核评估 | 📝 | - |
| 03 | 绩效管理助手 (Personio) | 目标拆解(KPI/OKR)→进度跟踪→达成差距分析→面谈提纲 | 📝📊 | app-user-mcp |
| 04 | 入职流程搭建器 (Onboarding Flow Builder) | 一键搭建入职审批应用（材料收集→审批→任务清单→试用期跟踪） | 🏗️⚡👥 | app-builder + app-user |
| 05 | 人力数据看板 (HR Analytics Dashboard) | 搭建人力分析看板（人员结构/流失率/招聘漏斗/培训完成率） | 🏗️📊 | app-builder + app-user |
| 68 | 薪酬分析 (Compensation Analytics) | 薪酬结构分析→市场对标→内部公平性诊断→人力成本预测→结果回写 | 📝📊⚡ | app-user-mcp |

**协作链路**：`01 招聘引擎 → 04 入职搭建器 → 02 培训设计师 → 03 绩效助手 → 05 人力看板 → 68 薪酬分析`

---

### 二、财务管理 (Finance)

> 覆盖报销、分析、应收应付、预算、发票、回款预测、SOX 审计全场景，AI 让财务从核算型走向分析型

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 06 | 报销审核助手 (Clawshier) | 报销单解析→票据校验→制度比对→异常识别→审核意见生成 | 📝📊 | app-user-mcp |
| 07 | 财务分析师 (Accounting) | 多表归集→差异分析→指标诊断→风险预警→分析报告 | 📝📊 | app-user-mcp |
| 08 | 应收应付管理 (Xero) | 账款汇总→账期管理→异常核查→催款话术→对账跟进 | 📝📊 | app-user-mcp |
| 09 | 预算编制助手 (Budget Planner) | 预算模板搭建→历史对比→审批流程→执行偏差预警→分析报告 | 📝📊🏗️⚡ | app-builder + app-user |
| 10 | 发票处理中心 (Invoice Processor) | 发票OCR识别→进销项匹配→税率校验→台账管理→自动入库 | 📊📦⚡ | app-user-mcp |
| 56 | 回款预测 (Collection Forecast) | 回款计划跟踪→逾期风险预测→催收策略→财务协同→状态回写 | 📝📊⚡ | app-user-mcp |
| 65 | SOX审计助手 (SOX Audit Assistant) | 控制测试设计→样本选取→工作底稿生成→缺陷评级→审计回写 | 📝📊⚡ | app-user-mcp |

**协作链路**：`10 发票处理 → 06 报销审核 → 09 预算助手 → 07 财务分析 → 08 应收应付 → 56 回款预测 → 65 SOX审计`

---

### 三、运营管理 (Operations)

> 覆盖数据分析、活动策划、用户反馈、SOP 管理、运营看板、流程诊断、经营汇报、智能客服、数据质量全链路

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 11 | 运营数据分析师 (Data Analysis) | 核心指标归集→波动识别→原因拆解→影响分析→复盘结论 | 📝📊 | app-user-mcp |
| 12 | 活动方案生成器 (CopyWriter) | 活动策划→文案输出→物料清单→执行流程→复盘框架 | 📝 | - |
| 13 | 用户反馈分析师 (Review Summarizer) | 反馈归集→问题分类→情绪判断→优先级排序→优化建议 | 📝📊 | app-user-mcp |
| 14 | 运营SOP生成器 (Automation Workflows) | 流程拆解→SOP模板→检查清单→风险标记→轻流流程落地 | 📝🏗️⚡ | app-builder + app-user |
| 15 | 运营看板搭建器 (KPI Dashboard Builder) | 看板设计→图表搭建→门户发布→数据分析→摘要读取 | 🏗️📊 | app-builder + app-user |
| 61 | 流程诊断 (Process Diagnostics) | 流程效率分析→卡点节点识别→超时预警→协同优化建议→结果回写 | 📝📊⚡ | app-user-mcp |
| 62 | 经营报告 (Business Report) | 经营数据汇总→周报/月报生成→经营趋势分析→改进事项跟踪 | 📝📊 | app-user-mcp |
| 63 | 智能客服 (Smart Customer Service) | 工单自动分类→知识库匹配→智能回复→转人工→满意度跟踪→看板搭建 | 📝📊⚡👥🏗️ | app-builder + app-user |
| 64 | 数据质量检测 (Data Quality Inspector) | 字段缺失率扫描→异常值检测→重复数据识别→治理建议→回写 | 📝📊⚡ | app-user-mcp |

**协作链路**：`11 数据分析 → 13 反馈分析 → 12 活动方案 → 14 SOP生成 → 15 看板搭建 → 61 流程诊断 → 62 经营报告 → 63 智能客服 → 64 数据质量`

---

### 四、销售管理 (Sales)

> 覆盖线索挖掘、客户画像、客户跟进、方案生成、CRM 搭建、赢输分析、录音分析全流程

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 16 | 销售线索挖掘 (AI Lead Generator) | 线索整理→意向筛选→分层分类→触达话术→跟进表 | 📝📊 | app-user-mcp |
| 17 | 客户跟进管理 (Sales Pipeline Tracker) | 跟进记录整理→阶段判断→异议提炼→话术生成→跟进清单 | 📝📊 | app-user-mcp |
| 18 | 销售方案生成 (Proposal Writer) | 需求提炼→方案框架→能力匹配→话术要点→方案摘要 | 📝 | - |
| 19 | 客户管理系统搭建器 (CRM App Builder) | 一键搭建完整CRM（客户/商机/跟进/合同/销售漏斗看板） | 🏗️📊⚡👥 | app-builder + app-user |
| 20 | 赢输单分析师 (Win-Loss Analyzer) | 成交/丢单原因归纳→竞品对比→策略建议→经验沉淀 | 📝📊 | app-user-mcp |
| 51 | 销售录音分析师 (Sales Call Analyzer) | 录音转写→话术评估→客户意向分析→关键信息提取→改进建议→数据回写 | 📝📊⚡ | app-user-mcp |
| 55 | 客户画像 (Customer Profile) | 客户信息建档→需求标签识别→销售准备材料→画像数据同步CRM | 📝📊⚡ | app-user-mcp |

**协作链路**：`16 线索挖掘 → 19 CRM搭建 → 55 客户画像 → 17 跟进管理 → 51 录音分析 → 18 方案生成 → 20 赢输分析`

---

### 五、市场营销 (Marketing)

> 覆盖内容生成、社媒管理、市场调研、SEO 优化、ROI 分析、AI 搜索诊断全链路

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 21 | 营销内容生成器 (Marketing Skills) | 选题策划→卖点提炼→多渠道文案→传播话术→发布建议 | 📝 | - |
| 22 | 社媒内容日历 (Social Media Content Calendar) | 活动方案→宣传文案→排期编排→物料清单→轻流搭建 | 📝🏗️ | app-builder |
| 23 | 市场调研分析师 (Competitive Intelligence) | 竞品归集→差异提炼→用户洞察→机会分析→调研结论 | 📝📊 | app-user-mcp |
| 24 | SEO内容优化师 (SEO Content Optimizer) | 关键词分析→标题优化→内容结构→元数据生成→策略建议 | 📝 | - |
| 25 | 活动ROI分析师 (Campaign ROI Analyzer) | 投放数据归集→ROI计算→渠道对比→优化建议→轻流看板 | 📝📊🏗️ | app-builder + app-user |
| 60 | AI搜索诊断 (AI Search Diagnostics) | 品牌提及监测→推荐排名分析→问答覆盖诊断→GEO优化策略 | 📝📊 | app-user-mcp |

**协作链路**：`23 市场调研 → 21 内容生成 → 24 SEO优化 → 60 AI搜索诊断 → 22 内容日历 → 25 ROI分析`

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

### 十一、生产制造 (Manufacturing)

> 覆盖智能排产、产能优化、交付预测、质量管控全场景，AI 赋能制造业从经验排产走向数据驱动

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 52 | 智能排产 (Smart Production Scheduler) | 订单排程编排→产能分配优化→计划冲突检测→插单影响分析→回写轻流 | 📝📊⚡ | app-user-mcp |
| 53 | 交付预测 (Delivery Prediction) | 订单进度跟踪→延期风险预测→延期原因分析→交付调整建议→风险回写 | 📝📊⚡ | app-user-mcp |
| 54 | 产能优化 (Capacity Optimization) | 设备负荷分析→瓶颈工序识别→班组调度优化→产能提升方案→分析回写 | 📝📊⚡ | app-user-mcp |
| 67 | 质量管控 (Quality Control) | 来料检验→过程巡检→不良分析→CAPA管理→质量系统搭建 | 📝📊⚡🏗️ | app-builder + app-user |

**协作链路**：`52 智能排产 → 54 产能优化 → 53 交付预测 → 67 质量管控`

---

### 十二、供应链 (SupplyChain)

> 覆盖需求预测、供应商履约、询价比价、库存优化全场景，AI 让供应链从被动响应走向主动预测

| # | Skill 名称 | 核心功能 | 能力标签 | MCP 依赖 |
|---|-----------|---------|---------|---------|
| 57 | 需求预测 (Demand Forecast) | 历史需求分析→需求量预测→缺货风险识别→补货建议→预测回写 | 📝📊⚡ | app-user-mcp |
| 58 | 履约预测 (Supplier Fulfillment) | 交期跟踪管理→延期风险预测→交付影响分析→应对措施建议→风险回写 | 📝📊⚡ | app-user-mcp |
| 59 | 询价比价 (Quotation Comparison) | 报价汇总整理→多维度比价→TCO总拥有成本分析→采购决策建议→比价回写 | 📝📊⚡ | app-user-mcp |
| 66 | 库存优化 (Inventory Optimization) | 安全库存测算→补货建议生成→ABC分类管理→库存周转分析→优化回写 | 📝📊⚡ | app-user-mcp |

**协作链路**：`57 需求预测 → 58 履约预测 → 59 询价比价 → 66 库存优化`

---

## 目录结构

```
skills/
├── 01-HR/                  # 人力资源（6 Skills）
├── 02-Finance/             # 财务管理（7 Skills）
├── 03-Operations/          # 运营管理（9 Skills）
├── 04-Sales/               # 销售管理（7 Skills）
├── 05-Marketing/           # 市场营销（6 Skills）
├── 06-Engineering/         # 技术研发（5 Skills）
├── 07-Product/             # 产品管理（5 Skills）
├── 08-Legal/               # 法务合规（5 Skills）
├── 09-ProjectMgmt/         # 项目管理（5 Skills）
├── 10-AdminIT/             # 行政与IT（5 Skills）
├── 11-Manufacturing/       # 生产制造（4 Skills）
└── 12-SupplyChain/         # 供应链（4 Skills）
```

每个 Skill 以独立 Markdown 文件呈现，包含：身份定义、能力描述、输入/输出示例、使用指令、轻流能力标签、MCP 依赖、协作链路等完整信息。

---

## 轻流 MCP 能力清单

> 基于当前可直接调用的 MCP 工具整理，覆盖运行态 + Builder + CLI 全能力。

### 一、@qingflow-tech/qingflow-cli — CLI 命令行工具

| 包名 | 用途 | 安装命令 | 适用 Skill 类型 |
|------|------|---------|----------------|
| `@qingflow-tech/qingflow-cli` | CLI 命令行工具，支持搭建 / 发布 / 调试 | `npm install @qingflow-tech/qingflow-cli` | Builder 类 Skill 的 CLI 辅助 |

| 能力 | 说明 |
|------|------|
| 认证登录 | 推荐使用 `auth_use_credential` 凭证接入，自动解析 token / wsId / qfVersion |
| 工作区切换 | 自动绑定工作区，必要时用 `workspace_select` 切换 |
| 应用调试 | 配合 Builder MCP 完成建模、发布、校验流程 |

---

### 二、@qingflow-tech/qingflow-app-user-mcp — 运行态能力

面向数据读写、任务处理、分析统计、导入导出等日常运行场景。

```bash
npm install @qingflow-tech/qingflow-app-user-mcp
```

#### 2.1 认证与工作区

| 工具 | 说明 |
|------|------|
| `auth_use_credential` | 凭证接入（推荐，自动解析 token / wsId / qfVersion） |
| `auth_logout` | 退出当前登录态 |
| `auth_whoami` | 查看当前身份与工作区 |
| `workspace_list` | 列出可用工作区 |
| `workspace_select` | 切换到目标工作区 |
| `workspace_get` | 获取当前工作区详情 |

#### 2.2 应用与门户读取

| 工具 | 说明 |
|------|------|
| `app_list` | 列出所有应用 |
| `app_get` | 获取单个应用详情 |
| `view_get` | 读取视图配置 |
| `chart_get` | 读取图表配置 |
| `portal_list` | 列出门户 |
| `portal_get` | 获取门户详情 |

#### 2.3 组织架构与人员目录

| 工具 | 说明 |
|------|------|
| `directory_search` | 统一目录搜索（部门 / 成员 / 外部联系人） |
| `record_member_candidates` | 获取成员字段候选范围 |
| `record_department_candidates` | 获取部门字段候选范围 |

#### 2.4 记录 CRUD

| 工具 | 说明 |
|------|------|
| `record_get` | 读取单条记录 |
| `record_list` | 列表浏览记录 |
| `record_access` | 基于视图的数据访问 |
| `record_insert` | 新增记录 |
| `record_update` | 更新记录 |
| `record_delete` | 删除记录 |
| `record_browse_schema_get` | 浏览字段 schema |
| `record_insert_schema_get` | 获取新增 schema |
| `record_update_schema_get` | 获取更新 schema |

#### 2.5 记录分析

| 工具 | 说明 |
|------|------|
| `record_access` | 基于字段 schema 的分析型查询，支持分组、聚合、统计、排序、筛选 |

#### 2.6 导入与导出

| 工具 | 说明 |
|------|------|
| `record_export_start` | 启动导出任务 |
| `record_export_status_get` | 查询导出状态 |
| `record_export_direct` | 直接导出 |
| `record_import_template_get` | 获取导入模板 |
| `record_import_schema_get` | 获取导入 schema |
| `record_import_verify` | 导入数据校验 |
| `record_import_repair_local` | 修复本地导入文件 |
| `record_import_start` | 启动导入 |
| `record_import_status_get` | 查询导入状态 |

#### 2.7 文件与附件

| 工具 | 说明 |
|------|------|
| `file_get_upload_info` | 获取上传信息 |
| `file_upload_local` | 上传本地文件（图片、附件、导入模板等） |

#### 2.8 任务与流程

| 工具 | 说明 |
|------|------|
| `task_list` | 查询任务列表 / 待办箱 |
| `task_get` | 获取任务详情 |
| `task_workflow_log_get` | 获取流程日志 |
| `task_associated_report_detail_get` | 获取关联报表明细 |
| `task_action_execute` | 执行任务动作（审批、转交、退回等） |

#### 2.9 代码块

| 工具 | 说明 |
|------|------|
| `record_code_block_schema_get` | 读取代码块 schema |
| `record_code_block_run` | 执行代码块（计算字段、外部查询回填等） |

---

### 三、@qingflow-tech/qingflow-app-builder-mcp — 搭建态能力

面向应用建模、流程配置、视图图表、门户发布等搭建场景。

```bash
npm install @qingflow-tech/qingflow-app-builder-mcp
```

#### 3.1 认证与工作区

| 工具 | 说明 |
|------|------|
| `auth_use_credential` | Builder 侧凭证接入 |
| `auth_logout` | Builder 侧退出登录 |
| `auth_whoami` | Builder 侧查看身份 |
| `workspace_list` | Builder 侧列出工作区 |
| `workspace_select` | Builder 侧切换工作区 |

#### 3.2 应用建模

| 工具 | 说明 |
|------|------|
| `app_schema_apply` | 创建 / 更新应用字段结构 |
| `app_layout_apply` | 配置表单段落与页面布局 |
| `app_flow_apply` | 配置审批流 / 自动化流程 |
| `app_views_apply` | 配置列表视图 / 看板视图 |
| `app_charts_apply` | 创建趋势图、漏斗图、饼图、柱状图等 |
| `app_publish_verify` | 发布前配置校验 |
| `app_resolve` | 按名称或 key 解析应用 |

#### 3.3 门户与解决方案包

| 工具 | 说明 |
|------|------|
| `portal_apply` | 创建 / 更新门户 |
| `portal_get` | 读取门户详情 |
| `portal_list` | 列出门户 |
| `portal_delete` | 删除门户 |
| `package_apply` | 创建 / 更新解决方案包 |
| `package_list` | 列出解决方案包 |
| `package_get` | 读取解决方案包详情 |
| `solution_install` | 安装打包的解决方案 / 模板 |

#### 3.4 角色与权限

| 工具 | 说明 |
|------|------|
| `member_search` | 搜索成员 |
| `role_create` | 创建角色 |
| `role_search` | 搜索角色 |

#### 3.5 辅助工具

| 工具 | 说明 |
|------|------|
| `builder_tool_contract` | 查询工具契约（别名、枚举、最小示例） |
| `app_custom_buttons_apply` | 创建 / 更新自定义按钮 |
| `button_style_catalog_get` | 查询按钮样式目录 |
| `app_repair_code_blocks` | 修复代码块配置 |
| `app_release_edit_lock_if_mine` | 释放发布编辑锁 |
| `app_get_fields` | 读取字段配置 |
| `app_get_layout` | 读取布局配置 |
| `app_get_views` | 读取视图配置 |
| `app_get_charts` | 读取图表配置 |
| `app_get_flow` / `app_flow_get` | 读取流程配置 |
| `app_flow_get_schema` | 读取流程 schema |
| `app_associated_resources_apply` | 关联资源应用 |
| `workspace_icon_catalog_get` | 查询工作区图标 / 颜色目录 |
| `feedback_submit` | 提交反馈（无需登录） |
| `file_upload_local` | Builder 侧上传本地文件 |

---

### 五大能力总结

| 能力类别 | 涵盖范围 | 关键工具 |
|---------|---------|---------|
| 🔄 运行态数据能力 | 读、写、删、分析、导入、文件上传、任务执行 | record_*, task_*, file_* |
| 👥 组织与权限支撑 | 成员目录、部门目录、成员候选、角色管理 | directory_*, member_*, role_* |
| 🏗️ Builder 建模能力 | 应用 schema、布局、流程、视图、图表、门户 | app_*_apply, portal_apply |
| ⚡ 自动化扩展能力 | 代码块、QLinker、流程动作、图表/门户展示 | record_code_block_*, task_action_* |
| 🔧 实施辅助能力 | 导入修复、编辑锁释放、发布校验、包管理 | record_import_*, package_*, app_publish_verify |

> 本清单按当前可直接调用的 MCP 工具整理，代表已接入并可用的能力范围。

---

## License

MIT

---

> **QingClaw × 轻流 — 让每个企业都拥有智能化的工作方式**
