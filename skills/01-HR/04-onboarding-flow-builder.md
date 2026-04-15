---
name: Onboarding Flow Builder
description: 轻流Builder深度集成——在轻流中一键搭建入职管理应用，包含材料收集表单、多级审批流程、入职任务清单、试用期跟踪。
color: teal
emoji: 🚀
vibe: 一句话描述入职需求，AI自动在轻流中搭建完整的入职审批应用
qingflow_mcp:
  - @josephyan/qingflow-app-builder-mcp
  - @josephyan/qingflow-app-user-mcp
---

# 🚀 入职流程搭建器 — Onboarding Flow Builder

## 安装方式

### 方式一：直接安装 MD 文件
将本文件放入 OpenClaw 的 skills 目录：
```
~/.openclaw/skills/04-onboarding-flow-builder.md
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
