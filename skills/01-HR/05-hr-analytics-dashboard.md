---
name: HR Analytics Dashboard
description: 轻流图表与门户深度集成——在轻流中搭建人力分析看板，覆盖人员结构、流失率、招聘漏斗、培训完成率等核心HR指标。
color: purple
emoji: 📊
vibe: 让HR用数据说话，在轻流中搭建人力资源核心指标看板
qingflow_mcp:
  - @josephyan/qingflow-app-builder-mcp
  - @josephyan/qingflow-app-user-mcp
---

# 📊 人力数据看板 — HR Analytics Dashboard

## 安装方式

### 方式一：直接安装 MD 文件
将本文件放入 OpenClaw 的 skills 目录：
```
~/.openclaw/skills/05-hr-analytics-dashboard.md
```
或直接将本 .md 文件发送给小龙虾（OpenClaw）即可使用。

### 方式二：连接轻流 MCP

```bash
# 安装轻流 MCP 包
npm install @josephyan/qingflow-app-builder-mcp@beta
npm install @josephyan/qingflow-app-user-mcp@beta

# 认证登录
# 方式A：账号密码登录 → auth_login
# 方式B：Token接入 → auth_use_token

# 选择工作区
# workspace_list → workspace_select
```
