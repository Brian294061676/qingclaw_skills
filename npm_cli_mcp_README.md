# Qingflow MCP Server

基于用户态会话上下文的 Qingflow MCP 适配层，覆盖表单数据、文件、应用、流程、视图、报表、门户、导航，以及高层解决方案搭建能力。

## 特性

- 用户账号登录，复用现有 Qingflow 权限模型
- 支持直接注入用户 `credential`，再通过 `/mcp/auth/context` 建立 MCP 会话
- 兼容直接注入用户 `token` 建立 MCP 会话
- 显式工作区选择，避免误用默认工作区
- 覆盖表单数据增查改删
- 覆盖内部成员 / 内部部门 / 外部联系人查询
- 覆盖 AI-native app builder 正式公开面：`package_get`、`package_apply`、`solution_install`、`builder_tool_contract`、`member_search`、`role_search`、`role_create`、`app_resolve`、`app_get`、`app_get_fields`、`app_get_layout`、`app_get_views`、`app_get_flow`、`app_get_charts`、`portal_list`、`portal_get`、`view_get`、`chart_get`、各类 `*_apply`、`app_release_edit_lock_if_mine`、`app_publish_verify`
- 覆盖待办发现、待办上下文摘要、统一待办动作执行、关联报表详情、流程日志查询
- 覆盖统一产品反馈提交：当当前能力不支持、流程不好用或诉求仍无法满足时，可在用户确认后通过 `feedback_submit` 提交需求反馈
- 覆盖门户 CRUD、门户发布
- 覆盖文件上传凭证获取与本地文件上传
- 内部继续保留 `solution_* / compiler / executor` 作为 builder 落地层，但不再作为公开 builder 主路径

## 不支持

- 外部部门查询
- 应用包内导航项配置
- 签名图片、eSign
- 外部成员候选查询（转交/加签）
- 短信验证码、多因素登录挑战
- OpenAPI `accessToken` / `serviceToken`

## 安装

```bash
cd <repo_root>/qingflow-support/mcp-server
python3 -m venv .venv
./.venv/bin/pip install -e '.[dev]'
```

## 本地智能体安装（npm）

如果你要给本地 agent / gateway 安装这套 MCP，而不是手动管理 Python 环境，可以直接安装统一 CLI 包，或两个独立 MCP 包：

```bash
npm install @qingflow-tech/qingflow-cli
npm install @qingflow-tech/qingflow-app-user-mcp
npm install @qingflow-tech/qingflow-app-builder-mcp
```

如果你在当前源码目录本地调试，也可以继续用：

```bash
cd <repo_root>/qingflow-support/mcp-server
npm install -g .
```

或只在当前目录安装：

```bash
cd <repo_root>/qingflow-support/mcp-server
npm install
```

如果你想把当前版本封装成可分发的 npm 安装包：

```bash
cd <repo_root>/qingflow-support/mcp-server
npm run pack:npm
```

产物会输出到：

```bash
dist/npm/qingflow-tech-qingflow-cli-<version>.tgz
dist/npm/qingflow-tech-qingflow-app-user-mcp-<version>.tgz
dist/npm/qingflow-tech-qingflow-app-builder-mcp-<version>.tgz
```

另一台机器可直接安装对应 tgz：

```bash
npm install /absolute/path/to/dist/npm/qingflow-tech-qingflow-cli-<version>.tgz
npm install /absolute/path/to/dist/npm/qingflow-tech-qingflow-app-user-mcp-<version>.tgz
npm install /absolute/path/to/dist/npm/qingflow-tech-qingflow-app-builder-mcp-<version>.tgz
```

安装时会自动创建 `.npm-python/`，并在里面执行 `pip install .`。

如果你是全局安装，完成后本机可直接使用这三个入口：

```bash
qingflow
qingflow-app-user-mcp
qingflow-app-builder-mcp
```

如果你只是对当前源码 checkout 执行了 `npm install`，请直接运行：

```bash
node ./npm/bin/qingflow.mjs --help
node ./npm/bin/qingflow-app-user-mcp.mjs
node ./npm/bin/qingflow-app-builder-mcp.mjs
```

适合这类本地 stdio MCP 客户端：

- Claude Desktop
- Cline / Cursor
- OpenClaw 风格的本地 agent / gateway
- 其它支持 `command + args + env` 的本地智能体

详细说明见：

- `docs/local-agent-install.md`

如果某个本地 MCP 客户端一调用工具就报 `Transport closed`，优先删掉安装目录里的 `.npm-python` 后重新 `npm install`，并确认 `@qingflow-tech/qingflow-cli`、`@qingflow-tech/qingflow-app-user-mcp`、`@qingflow-tech/qingflow-app-builder-mcp` 没有混用不同版本。stdio MCP 入口现在会拒绝在启动瞬间重建 Python 运行时，避免安装日志写进 stdout 破坏 MCP 握手。

## 运行

```bash
cd <repo_root>/qingflow-support/mcp-server
./qingflow-app-user-mcp
```

或：

```bash
qingflow --help
qingflow-app-user-mcp
qingflow-app-builder-mcp
```

## 配置

- `QINGFLOW_MCP_DEFAULT_BASE_URL`：默认 Qingflow 后端地址
- `QINGFLOW_MCP_DEFAULT_QF_VERSION`：默认 `qfVersion` 路由值
- `QINGFLOW_MCP_HOME`：本地会话目录，默认 `~/.qingflow-mcp`
- `QINGFLOW_MCP_DESIGN_HOME`：`solution_design_session` 本地设计会话目录，默认 `~/.qingflow-mcp/design-sessions`
- `QINGFLOW_MCP_BUILD_HOME`：分阶段 build assembly 目录，默认 `~/.qingflow-mcp/build-assemblies`
- `QINGFLOW_MCP_BOOTSTRAP_HOME`：`solution_bootstrap` 运行记录目录，默认 `~/.qingflow-mcp/bootstrap-runs`
- `QINGFLOW_MCP_TIMEOUT_SECONDS`：HTTP 超时秒数，默认 `30`
- `QINGFLOW_MCP_FEEDBACK_QSOURCE_TOKEN`：反馈表 q-source 被动入口 token；当前包已内置默认反馈通道，通常无需单独配置，只有在你要覆盖默认通道时才需要设置
- `QINGFLOW_MCP_FEEDBACK_BASE_URL`：反馈提交使用的 base URL，默认回退到 `QINGFLOW_MCP_DEFAULT_BASE_URL`
- `QINGFLOW_MCP_FEEDBACK_APP_KEY`：内部反馈表 app_key，默认 `e0d017kju002`
- `QINGFLOW_MCP_CREDIT_METER_ENABLED`：是否启用工具调用计费，默认 `true`
- `QINGFLOW_MCP_CREDIT_APAAS_BASE_URL`：调用记录接口系统地址，默认使用当前登录会话的 Qingflow 后端地址
- `QINGFLOW_MCP_CREDIT_APAAS_PATH`：调用记录接口路径，默认 `POST /user/credit/usage`

说明：
- 计费逻辑只在“顶层工具调用”触发一次，内部嵌套调用不会重复扣费。
- usage 记录接口使用当前登录会话的 `token` 与 `wsId` 请求头。
- usage 记录接口固定上报：`skuType=MCP`、`skuName=MCP`、`modelName=MCP`、`scene=MCP`、`aiBiz=MCP`，`extraInfo` 为当前 tools 方法名。

会话信息写入 `~/.qingflow-mcp/profiles.json`，包括 `token` / `login_token` / `credential` / `base_url` / `wsId` / `qfVersion` 等后续 CLI 命令恢复会话所需字段。

配置文件会按下面的顺序查找第一个存在的文件：

1. `QINGFLOW_MCP_CONFIG_PATH`
2. 当前工作目录 `qingflow-mcp.config.json`
3. `~/.qingflow-mcp/config.json`
4. `/etc/qingflow-mcp/config.json`

`auth_use_credential` 的路由优先级是：

1. 工具参数里显式传入的 `base_url` / `qf_version`
2. 全局默认 `QINGFLOW_MCP_DEFAULT_BASE_URL` / `QINGFLOW_MCP_DEFAULT_QF_VERSION` 或配置文件里的 `default_base_url` / `default_qf_version`（同层里环境变量优先）

敏感 `token` / `credential` 会随 profile 写入 `profiles.json`；`persist=true` 时还会优先同步写入系统 keychain，keychain 不可用时仍可从 profile 文件恢复 CLI 会话。

示例配置文件：

```json
{
  "default_base_url": "https://qingflow.com/api",
  "default_qf_version": "canary",
  "credit_meter": {
    "enabled": true,
    "apaas": {
      "base_url": "https://apaas.internal.example.com",
      "path": "/user/credit/usage"
    }
  },
  "feedback": {
    "qsource_token": "replace-with-your-qsource-token",
    "app_key": "e0d017kju002"
  }
}
```

可直接复制的模板文件见：[qingflow-mcp.config.example.json](/Users/qingflow/IdeaProjects/qingflow-next/qingflow-support/mcp-server/qingflow-mcp.config.example.json)。

三套环境变量模板（可直接复制）：

```bash
# dev
export QINGFLOW_MCP_CREDIT_METER_ENABLED=true
export QINGFLOW_MCP_CREDIT_APAAS_BASE_URL="https://apaas-dev.internal.example.com"
export QINGFLOW_MCP_CREDIT_APAAS_PATH="/user/credit/usage"
```

```bash
# staging
export QINGFLOW_MCP_CREDIT_METER_ENABLED=true
export QINGFLOW_MCP_CREDIT_APAAS_BASE_URL="https://apaas-staging.internal.example.com"
export QINGFLOW_MCP_CREDIT_APAAS_PATH="/user/credit/usage"
```

```bash
# prod
export QINGFLOW_MCP_CREDIT_METER_ENABLED=true
export QINGFLOW_MCP_CREDIT_APAAS_BASE_URL="https://qingflow.com/api"
export QINGFLOW_MCP_CREDIT_APAAS_PATH="/user/credit/usage"
```

## 会话模型

1. 调用 `auth_use_credential`
2. 使用 `/mcp/auth/context` 返回的 `wsId` / `qfVersion` 建立本地会话
3. 再调用业务工具

说明：
- 本地模式推荐优先使用 `auth_use_credential`。典型来源是 createClaw 在本地保存并注入 `credential`，MCP 再调用 `/mcp/auth/context` 解析出 `token`、`wsId`、`qfVersion`、`uid` 等上下文。
- `auth_use_credential` 是 MCP 工具，不是额外的 HTTP 请求头。业务请求真正发送的是解析后的 `token`、`wsId`，以及必要时的 `Cookie: qfVersion=...`
- 本地模式下，`/mcp/auth/context` 返回的 `wsId` / `qfVersion` 是当前会话的唯一权威来源
- 如果当前能力不支持、流程明显不好用，或用户诉求在合理尝试后仍无法满足，智能体应先简短总结 gap，再询问是否提交需求反馈；只有在用户明确确认后，才调用 `feedback_submit`

## 工具清单

### 认证与工作区

- `auth_use_credential`
- `auth_whoami`
- `auth_logout`
- `workspace_list`
- `workspace_set_plugin_status`

### 反馈

- `feedback_submit`

说明：
- `feedback_submit` 通过 q-source 被动入口把反馈写入内部反馈表，不走直写记录工具
- 该工具不要求先登录或选择工作区
- 推荐字段包括：标题、分类、问题描述、期望结果、当前实际情况、影响范围、相关工具、应用/记录/节点上下文
- 提交前应先得到用户明确确认

### 应用发现与可访问视图

- `app_list`
- `app_search`
- `app_get`

说明：
- `app_get` 返回当前 app 的基础能力地图，包括：
  - `can_create`：当前用户是否可走普通 applicant/create 路径发起数据
  - `accessible_views`：当前用户在该 app 下真实可访问的数据视图列表
- `accessible_views` 统一合并：
  - 系统视图：如 `全部数据 / 我发起的 / 待办 / 已办 / 抄送我的`
  - 自定义视图：如业务上配置的区域、团队、专题视图
- 每个 `accessible_views` 项会返回 `analysis_supported`
  - `true`：可用于 `record_analyze`
  - `false`：仅适合浏览，不适合分析
- `boardView`、`ganttView` 会直接标记为 `analysis_supported=false`
- 后续 `record_list / record_get / record_analyze / record_browse_schema_get` 应优先使用 `app_get.accessible_views` 里的 `view_id`
- 当 `view_id=custom:*` 时，MCP 会显式返回：
  - `verification.scope_source = "custom_view"`
  - `verification.view_filter_verified = false`
  - `warnings += CUSTOM_VIEW_FILTER_UNVERIFIED`
- 这表示 custom view 仍可用作便捷取数入口，但 MCP 不把它当成“后端已验证 saved-filter 口径”的强可信范围
- 业务关键分析默认优先 `system:all + explicit filters`；若仍使用 custom view，结论中应明确说明筛选可信度未验证

### 表单数据

- `record_insert_schema_get`
- `record_update_schema_get`
- `record_browse_schema_get`
- `record_code_block_schema_get`
- `record_import_schema_get`
- `record_member_candidates`
- `record_department_candidates`
- `record_analyze`
- `record_list`
- `record_get`
- `record_insert`
- `record_update`
- `record_delete`
- `record_code_block_run`
- `record_import_template_get`
- `record_import_verify`
- `record_import_repair_local`
- `record_import_start`
- `record_import_status_get`

说明：
- `record_insert_schema_get` 是 `record_insert` 的唯一默认 schema 入口，返回 **insert-ready schema**：默认只看 `required_fields / optional_fields / runtime_linked_required_fields / payload_template`
- `record_update_schema_get` 是 `record_update` 的唯一默认 schema 入口，返回 **当前 record 在 matched accessible views 下的整体可更新字段集合**：默认只看 `writable_fields / payload_template`
- `record_browse_schema_get(view_id=...)` 返回**指定浏览视图下的 browse schema**，用于 `record_list / record_get / record_analyze`
- `record_code_block_schema_get` 返回代码块执行前需要的 code-block-ready schema
- `record_import_schema_get` 返回导入场景的 import-ready column schema
- 隐藏字段不会出现在 schema 中；缺失字段应解释为当前用户在当前 schema 口径下不可见/不可用，而不是继续猜 builder 全字段
- relation 字段在 insert/update schema 中会尽力返回 `target_app_key / target_app_name / searchable_fields`，用于明确它实际引用的目标应用与可搜索字段；这只解决目标发现，不等于 relation 写入协议已经自动推断完毕
- member / department 字段默认支持直接传自然值；只有在需要显式浏览候选、或写入返回歧义确认时，再走 `record_member_candidates` / `record_department_candidates`
- `record_member_candidates` / `record_department_candidates` 仍以 applicant-node 当前字段的候选范围为基线，默认全部时也优先走业务搜索链路，而不是要求先成功访问 `directory_*`
- 当 member / department 字段的候选范围可安全解析时，`record_insert / record_update` 会按字段候选范围做写入校验；超出候选范围的名字或 id 会在 MCP 侧直接拦截，不再把请求送到后端后才报 `40002`
- 如果 member / department 候选读取本身失败，`record_insert / record_update` 也会直接返回候选读取错误；只有字段候选范围本身不支持时，才会回退到旧写入行为
- `directory_*` 更适合作为通讯录浏览、组织结构查看或兜底排查工具，而不是 member / department 字段选择的默认起点
- member / department 字段的动态或外部联系人范围仍然 fail-closed
- `record_analyze` 是统一分析入口；传 `dimensions=[]` 表示整表 summary，传 `dimensions!=[]` 表示 grouped analysis。字段引用只接受 `field_id`
- 如果所选 `view_id` 对应 `boardView` 或 `ganttView`，`record_list` 和 `record_analyze` 都会直接返回不支持；此时应改选系统视图或表格类自定义视图
- 如果所选 `view_id` 是 custom view，`record_list / record_get / record_analyze` 仍可执行，但返回会显式标记 `CUSTOM_VIEW_FILTER_UNVERIFIED`；不要把 custom view 的筛选结果当成已验证事实
- `record_list` 只用于列表浏览、导出和样本检查；它使用字段级 `columns / where / order_by` JSON DSL，不承担分析结论
- browse / analyze 的 canonical 范围选择参数是 `view_id`
- `view_id` 统一来自 `app_get.accessible_views`
- `list_type / view_key / view_name` 的 compatibility-only 语义仅保留在 browse / analyze 读路径；`record_update` 不再接受任何 `view_*` 选择参数
- `record_list` / `record_get` 的 `columns` 规范写法是 `[{ "field_id": 12 }]`
- `record_list.where` 的规范写法是 `{ "field_id": 12, "op": "eq", "value": "进行中" }`
- `record_list.order_by` 的规范写法是 `{ "field_id": 18, "direction": "desc" }`
- 兼容性的裸整数 `field_id`、`fieldId`、`operator`、`values`、`order` 仍可解析，但会返回 legacy warning；新调用一律使用规范写法
- `record_get` 用于按 `record_id` 读取单条记录；当只需要部分列时，也只接受 `field_id` 列选择；不传 `columns` 时也只返回 applicant-aware 可见字段
- `record_analyze` 会统一返回 `query / result / ranking / ratios / completeness / presentation`，并隐藏分页与扫描预算等执行细节；模型只需要表达分析意图，不需要手动填写 `page_size / requested_pages / scan_max_pages / auto_expand_pages`
- `record_insert` 的标准路径是 `record_insert_schema_get -> record_insert`
- `record_update` 的标准路径是 `record_update_schema_get -> record_update`
- `record_insert` 使用 applicant-node `fields` map；它不接受任何 `view_*` 选择器
- `record_insert_schema_get.optional_fields` 里若出现 `may_become_required=true`，表示该字段仍然可直写，但在联动可见性或 option 规则触发后可能变成运行时必填；这类字段会额外带 `requirement_reason / activation_sources`
- `record_insert_schema_get.runtime_linked_required_fields` 只表示“必填、不可直写、通常依赖运行时联动或上游上下文补值”的字段；不要把它们当成普通手填字段
- `record_update` 使用字段标题 keyed 的 `fields` map，并在内部按当前 payload 自动选择第一个可执行的 matched accessible view；调用方不再传任何 `view_*` 选择参数
- `record_update_schema_get` 返回的是字段全集 schema，不保证其中任意字段组合都能一次成功；最终是否可更新，仍取决于是否存在单一 matched accessible view 能覆盖该 payload
- `record_delete` 只接受 `record_id / record_ids`，不接受任何 `view_*` 选择器
- 三个直写工具都会先做内部静态预检；如果有 blockers，会返回 blocked 响应且**不会**写入数据；对当前 schema 中不存在或 `writable=false` 的字段会直接拒绝
- 直写成功时才真正 apply；若 `ok=false`，应先检查 `field_errors / blockers / warnings / normalized_payload`
- 对 insert/update 的读回验证，如果需要和写入形态做语义一致对比，优先使用 `record_get(..., output_profile="normalized")` 或 `record_list(..., output_profile="normalized")`
- `normalized` 读回会把常见后端返回归一成更接近写入形态的结构：
  - 日期 `YYYY-MM-DD 00:00:00` 会归一成 `YYYY-MM-DD`
  - 多选始终归一成数组
  - 地址始终归一成 `{province, city, district, detail}`
  - 子表始终归一成“父字段 -> 行数组”，并去掉 `__row_id__` 和 `-` 开头的衍生列
  - relation 会归一成 `{apply_id, label}`
- `record_code_block_run` 用于执行表单中的代码块字段（`queType=26`）
- 标准路径是：
  - `record_code_block_schema_get`
  - 选择精确的代码块字段
  - `record_code_block_run`
- 该工具会先读取当前记录答案，再调用后端代码块执行链路；如果代码块绑定了 `questionRelations.relationType=3` 的关联目标，MCP 会继续触发关系计算并自动写回目标字段
- 因此 `record_code_block_run` 不是纯只读工具，应把它视为“执行 + 可能自动回写”的操作
- 在流程上下文中运行代码块时，应传 `role=3` 和精确的 `workflow_node_id`
- 执行后应优先检查：
  - `outputs.alias_results`
  - `relation.target_fields`
  - `writeback.applied`
  - `writeback.verification`
- 子表字段继续使用“父字段 -> 行数组”写法，例如 `{\"销售明细\": [{\"产品名称\": \"企业版\", \"数量\": 2}]}`；更新既有子表行时可额外传 `rowId / row_id / __row_id__`
- 导入统一走：
  - `app_get`
  - `record_import_template_get`
  - `record_import_verify`
  - `record_import_repair_local`
  - `record_import_start`
  - `record_import_status_get`
- 导入前先看 `app_get.data.import_capability`
- 如果 `import_capability.can_import=false`，不要继续做模板下载、文件修复或导入启动
- `record_import_start` 不接受原始文件路径，只接受成功校验后的 `verification_id`
- `record_import_start` 的 `being_enter_auditing` 必须显式传入；不要在客户端侧假设默认值
- 未经用户明确授权，不允许修改用户上传的导入文件
- 若用户授权修复文件，MCP 只允许做安全格式修复，并且默认保留原文件、输出修复副本，再重新执行 `record_import_verify`

### 待办与审批上下文

- `task_list`
- `task_get`
- `task_action_execute`
- `task_associated_report_detail_get`
- `task_workflow_log_get`

说明：
- task 主路径从 `task_list` 开始；它会返回归一化后的 `task_id / app_key / record_id / workflow_node_id`
- `task_get` 用于读取单条待办的节点上下文摘要，包括可执行动作、字段权限、记录详情、关联报表摘要、流程日志摘要，以及回退/转交候选摘要
- `task_action_execute` 是统一动作入口；当前只支持 `approve / reject / rollback / transfer / urge`
- `task_action_execute` 现在显式区分“动作执行成功”和“续流验证成功”
  - 若动作执行成功但没有足够证据证明下游待办或状态已继续流转，会返回 `partial_success`
  - 同时带 `warnings += WORKFLOW_CONTINUATION_UNVERIFIED`
  - 并设置 `verification.runtime_continuation_verified = false`
- 如果后端返回 `46001 已被他人处理`，MCP 会先尝试回读记录状态、流程日志和任务上下文
  - 若能证明记录已继续流转，会返回兼容性的部分成功
  - 若仍无法证明，则返回 `TASK_CONTEXT_VISIBILITY_UNVERIFIED`，而不是直接把它当成“已被处理”的事实
- task 动作一律使用 `app_key + record_id + workflow_node_id`，不要把 `task_id` 直接当作审批主键
- `task_associated_report_detail_get` 会区分关联视图和关联报表：
  - 关联视图返回 `result_type=view_list`，结果尽量对齐 `record_list`
  - 关联报表返回 `result_type=chart_data`，并保留图表型结果结构
- `task_workflow_log_get` 返回当前待办上下文下的流程日志明细；若节点日志不可见，会明确报错

### 文件

- `file_get_upload_info`
- `file_upload_local`

### 应用

- `package_list`
- `package_get`
- `package_get_base`
- `package_create`
- `package_update`
- `package_delete`

说明：
- 上面这些 `package_*` 是低层原生接口，主要用于原生接口对照和内部调试，不是当前 builder 正式公开 contract
- 当前 builder 面向智能体的 package 正式入口统一使用 `package_get` / `package_apply`
- `package_apply` 统一承接应用包创建、改名、图标、可见权限、分组布局、app/portal 挂载与排序编排
- `package_get` 会优先读真实布局；如果 detail 接口不可读，会降级到 `baseInfo` 并返回 warning，而不是假装读到了完整 detail

- `navigation_list_published`
- `navigation_list_draft_page`
- `navigation_list_draft_all`
- `navigation_get_detail`
- `navigation_get_status`
- `navigation_set_visible`
- `navigation_create`
- `navigation_update`
- `navigation_delete`
- `navigation_publish`
- `navigation_reorder`

说明：
- `workspace_set_plugin_status` 会调用工作区插件安装接口，可用于安装或卸载指定插件。
- staged 高层 build 在创建导航时如果遇到 `50004 插件未安装`，会先尝试自动安装导航插件，再重试一次导航创建。
- builder public flow 路径现在支持：
  - `member_search` / `role_search` 访问通讯录成员与角色
  - `role_create` 创建并复用角色
  - `app_flow_apply` 为审批、填写、抄送节点显式声明负责人，优先角色，也支持指定成员
  - `permissions.editable_fields` 显式配置节点内可编辑字段

- `app_list`
- `app_search`
- `app_get_base`
- `app_update_base`
- `app_get_form_schema`
- `app_create`
- `app_delete`
- `app_publish`

说明：
- `app_list` / `app_search` 用于列出当前工作区内、当前登录用户可见的应用；当 `app_key` 未知时，优先先做应用发现
- `app_get_base` 和 `app_get_form_schema` 默认返回紧凑摘要，适合智能体消费；如果需要完整原始 `baseInfo/form schema`，显式传 `include_raw=true`
- 原始表单 schema 写入接口 `app_update_form_schema` 已不再对外暴露；对外应优先使用 `solution_*` 或更高层的 builder 流程，而不是直接拼接原生 schema

### 流程

- `workflow_list_nodes`
- `workflow_get_node_detail`
- `workflow_get_global_settings`
- `workflow_get_future_nodes`
- `workflow_get_future_nodes_app`
- `workflow_get_qsource_active`
- `workflow_get_qsource_passive`
- `workflow_get_editable_question_ids`
- `workflow_get_print_nodes`

说明：
- `workflow_*` 的低层写接口已不再对外暴露；对外应优先使用 `solution_build_flow`

### 视图

- `view_list`
- `view_list_flat`
- `view_get_config`
- `view_get_base_info`
- `view_list_questions`
- `view_list_associations`
- `view_board_get_lane_base_info`
- `view_get_future_nodes`
- `view_get_workflow_status`

说明：
- `view_*` 的低层写接口已不再对外暴露；对外应优先使用 `solution_build_views`

### 报表

- `qingbi_report_list`
- `qingbi_report_get_base`
- `qingbi_report_get_config`
- `qingbi_report_get_data`
- `qingbi_report_delete`
- `qingbi_report_reorder`
- `qingbi_report_list_fields`
- `qingbi_report_list_field_options`

说明：
- `qingbi_report_*` 的原始创建和配置写入接口已不再作为公开 builder 主路径；对外应优先使用 `app_charts_apply`

### 门户

- `portal_list`
- `portal_get`
- `portal_create`
- `portal_update`
- `portal_delete`
- `portal_publish`

说明：
- `portal_*` 的低层写接口不建议作为公开 builder 主路径；对外应优先使用 `portal_apply`

### 通讯录

- `directory_search`
- `directory_list_internal_users`
- `directory_list_all_internal_users`
- `directory_list_internal_departments`
- `directory_list_all_departments`
- `directory_list_sub_departments`
- `directory_list_external_members`

### AI-native App Builder

公开 builder 面现在只保留资源型 `get/apply` 工具和少量解析/辅助工具：

- package：
  `package_get`、`package_apply`
- solution / directory：
  `solution_install`、`member_search`、`role_search`、`role_create`
- app：
  `app_resolve`、`app_get`、`app_get_fields`、`app_get_layout`、`app_get_views`、`app_get_flow`、`app_get_charts`、`app_repair_code_blocks`、`app_release_edit_lock_if_mine`
- button：
  `app_custom_button_list`、`app_custom_button_get`、`app_custom_button_create`、`app_custom_button_update`、`app_custom_button_delete`
- portal / view / chart：
  `portal_list`、`portal_get`、`view_get`、`chart_get`
- apply / verify：
  `app_schema_apply`、`app_layout_apply`、`app_flow_apply`、`app_views_apply`、`app_charts_apply`、`portal_apply`、`app_publish_verify`

推荐顺序：

1. package：
   已知 `package_id` 时先 `package_get`；需要创建或整体更新应用包时直接使用 `package_apply`
2. app：
   先 `app_resolve`，再按需要读取 `app_get` / `app_get_fields` / `app_get_layout` / `app_get_views` / `app_get_flow` / `app_get_charts`
3. portal / view / chart：
   分别使用 `portal_get` / `view_get` / `chart_get`
4. 写入：
   按资源类型调用对应 `*_apply`
5. 核验：
   app 类写入后按需要再调用 `app_publish_verify`

统一 `visibility` contract：

- `package`、`app`、`view`、`chart`、`portal` 都支持统一的公开 `visibility` 写法
- 统一语义为：
  - `mode = workspace | everyone | specific`
  - `external_mode = not | workspace | specific`
- builder public contract 以 `visibility` 为准，不鼓励直接写后端 raw `auth`
- `portal_apply.auth` 仅作为兼容别名保留；新调用统一使用 `visibility`

`package_apply` 行为模型：

- `package_id` 是编辑已有应用包的正式入口
- `create_if_missing=true + package_name` 是创建新应用包的正式入口
- `items` 表示目标完整布局，而不是增量 diff
- 若省略现有 app / portal 且未传 `allow_detach=true`，会直接阻塞写入
- 未显式提供 `group_id` 时，会尽量复用现有分组；若同名分组存在歧义，会返回结构化错误而不是猜

Builder 结果解释规则：
- 所有 AI-native Builder 工具现在统一返回 `warnings`、`verification`、`verified`
- 读工具在可返回主体数据但部分读回不可用时，仍可能是 `status=success` 且 `verified=false`；此时应优先看 `warnings` 和 `verification`
- `app_charts_apply`、`portal_apply`、`app_publish_verify` 等写入/核验工具中，`success` 表示写入且验证完成；`partial_success` 表示写入已执行但验证不完整

约束：

- `app_schema_apply` 是唯一允许创建 app 壳的公开 patch 工具
- 应用壳创建通过 `app_schema_apply(package_id + app_name + create_if_missing=true)` 完成
- 门户创建通过 `portal_apply(package_id + dash_name)` 完成
- 应用包创建、改名、权限更新、分组布局和 app/portal 挂载通过 `package_apply` 完成
- `app_schema_apply` / `app_layout_apply` / `app_flow_apply` / `app_views_apply` 内部会先执行服务端 planning / normalization / dependency checks；如果预检查不通过，直接返回 blocking issues 和下一步建议
- 默认自动发布只发生在“实际有变更”的 apply 上；空操作不会触发发布
- `app_schema_apply` 在结果 schema 中检测到多个 `relation` 字段时，会返回 `warnings += RELATION_FIELD_LIMIT_RISK`，并在 `verification.relation_field_limit_verified=false` 中显式提示风险；若后端返回已知 `49614`，MCP 会归一化成 `MULTIPLE_RELATION_FIELDS_UNSUPPORTED`
- `app_charts_apply` 用于 QingBI 图表的增删改排序，图表即时生效，不单独发布；图表定位优先级为 `chart_id > 精确名称匹配`，同名不唯一时必须显式传 `chart_id`
- `app_get_charts` 用于读取当前应用下图表摘要，适合在 `app_charts_apply` 前先确认现有 `chart_id`
- `portal_apply` 用于门户页面，采用整页 replace 模型；删除 section 通过 omission 完成，`publish=false` 只保证 draft/base info 更新，`publish=true` 时发布草稿并校验 live；`chart_ref/view_ref` 按 `id/key` 优先、名称回退，名称不唯一时会直接失败
- `portal_get` 用于读取门户草稿或 live 详情，默认读 draft；`portal_list` 用于先发现当前工作区可配置门户
- `app_layout_apply` 默认 `mode=merge`，会保留未显式编排的现有字段；只有 `mode=replace` 才要求你一次覆盖全部字段
- `app_layout_apply` 的验证现在区分：
  - `verification.layout_verified`
  - `verification.layout_summary_verified`
  如果 compact summary 不可信但 raw form readback 仍能证明布局字段序列已落地，会返回 `partial_success + LAYOUT_SUMMARY_UNVERIFIED`
- `app_layout_apply / app_flow_apply / app_views_apply` 只作用于已存在 app
- `relation` 必须显式提供 `target_app_key`
- `subtable` 必须显式提供 `subfields`
- `app_schema_apply / app_layout_apply / app_flow_apply / app_views_apply` 默认自动发布；只有传 `publish=false` 才保留草稿
- `app_views_apply` 现在明确分离：
  - `verification.views_verified`
  - `verification.view_filters_verified`
  视图存在不等于视图筛选已验证；若 filter readback mismatch，会返回 `partial_success` 和 `VIEW_FILTERS_UNVERIFIED`
- `app_flow_apply` 现在只公开支持前端稳定可显示的线性流程节点：
  - `start`
  - `approve`
  - `fill`
  - `copy`
  - `webhook`
  - `end`
  `branch` 和 `condition` 已在公开 MCP 能力里禁用；若传入会直接返回 `FLOW_NODE_TYPE_UNSUPPORTED`
- `app_publish_verify` 仍保留为显式发布验收工具

设计边界：

- 公开面只讲资源、摘要读和 patch 计划，不再暴露 `build_id/mode/stage/repair`
- 内部继续复用 `solution_* / compiler / executor`
- `solution_*` 仍保留在代码里，但不再作为公开 builder 主路径
- 不推荐直接使用低层 `qingbi_report_*` 或 `portal_*` 写接口完成日常 builder 工作流

## 示例 MCP client 配置

见 `examples/claude_desktop_config.json`。

如果通过 npm 安装到本机，也可以直接配成：

```json
{
  "mcpServers": {
    "qingflow-user": {
      "command": "qingflow-app-user-mcp",
      "args": [],
      "env": {
        "QINGFLOW_MCP_DEFAULT_BASE_URL": "https://qingflow.com/api"
      }
    }
  }
}
```

## 示例调用顺序

见 `examples/transcript.md`。

## 设计文档

- 工具矩阵与后续扩展方案：`docs/tool-matrix.md`

## 典型用法

### 1. 注入 credential

推荐给 createClaw 或其它本地宿主使用：

```json
{
  "profile": "default",
  "base_url": "https://qingflow.example.com/api",
  "credential": "1602853_277941",
  "persist": false
}
```

MCP 会用这个 `credential` 调用 `/mcp/auth/context`，自动解析并保存：

- `token`
- `credential`
- `base_url`
- `uid`
- `ws_id`
- `ws_name`
- `qf_version`

### 2. 查询工作区

```json
{
  "profile": "default",
  "page_num": 1,
  "page_size": 20,
  "if_mongo": false
}
```

`if_mongo=false` queries the all-version internal workspace list.
`if_mongo=true` switches to the mongo-oriented workspace list, which may also include external workspaces.
`include_external` remains supported as a legacy alias, but the name is misleading because it changes the backend data source rather than simply appending external workspaces.

### 3. 选择工作区

```json
{
  "profile": "default",
  "ws_id": 10001
}
```

### 4. 新增记录

```json
{
  "profile": "default",
  "app_key": "APP_xxx",
  "submit_type": 1,
  "answers": [
    {
      "queId": 1001,
      "queType": 2,
      "values": [{ "value": "hello" }],
      "tableValues": []
    }
  ]
}
```

### 5. 搜索内部成员

```json
{
  "profile": "default",
  "keyword": "张",
  "page_num": 1,
  "page_size": 20,
  "include_disabled": false
}
```

### 6. 拉取全部内部成员

```json
{
  "profile": "default",
  "page_size": 200,
  "max_pages": 100,
  "include_disabled": false
}
```

### 7. 拉取全部部门树

```json
{
  "profile": "default",
  "parent_department_id": null,
  "max_depth": 20,
  "max_items": 2000
}
```

## 返回约定

- 成功时返回结构化 JSON
- Qingflow 后端报错会原样透出主要错误信息
- token 失效时会自动清除当前 profile 的本地会话，并提示重新登录

## 本地 createClaw 接入

如果本地智能体是由 createClaw 创建和托管，推荐接入方式是：

1. createClaw 为当前实例保存一份 `credential`
2. 本地 MCP 启动后，调用 `auth_use_credential`
3. MCP 再调用 apaas `/mcp/auth/context`
4. 得到当前实例对应的 `token / wsId / qfVersion / uid`
5. 后续业务工具直接使用这份上下文

说明：

- 这是本地模式唯一鉴权主路径
- 如果后续本地会话要做自动 refresh，也应优先基于已保存的 `credential`
