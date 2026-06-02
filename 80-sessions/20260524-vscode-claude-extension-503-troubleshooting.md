# VS Code Claude Code 扩展 503 问题排查记录

**日期**: 2026-05-24

## 问题现象

| 环境 | 贵价模型 | 便宜模型 |
|------|---------|---------|
| 终端 `claude` | 正常 | 正常 |
| 桌面启动 VS Code → 扩展插件 | 正常 | **503** |
| 桌面启动 VS Code → 内置终端 `claude` | 正常 | 正常 |
| 终端 `code .` 启动 VS Code → 扩展插件 | 正常 | 正常 |

## 关键信息

- **终端 CLI 版本**: 2.1.150
- **VS Code 扩展版本**: 2.1.145.688
- **中转站**: `https://www.micuapi.ai`
- **配置位置**: `~/.claude/settings.json` (env 字段)
- **认证方式差异**: 终端 CLI 直接使用 API Key (Authorization header)，VS Code 扩展走 OAuth 流程

## 日志关键发现

```
[API REQUEST] /v1/messages source=sdk
cc_version=2.1.145.688; cc_entrypoint=claude-vscode
ANTHROPIC_CUSTOM_HEADERS present: false, has Authorization header: false
[API:auth] OAuth token check starting

API error (attempt 1/11): 503
No available channel for model claude-opus-4-6 under group vip_2 (distributor)
```

扩展被路由到 `vip_2` 组，而终端被路由到 `vip_1_max_enterprise` 组。

**根因**：中转站（micuapi.ai）根据认证方式做差异化路由——**OAuth 认证分配到 `vip_2` 组（模型少）**，**API Key 认证分配到 `vip_1_max_enterprise` 组（模型全）**。终端 CLI 使用 API Key，而 VS Code 扩展默认走 OAuth。

## 解决方案演进

### 方案一（无效）：仅设 `ANTHROPIC_BASE_URL`

只设 `ANTHROPIC_BASE_URL` 不能让扩展跳过 OAuth，请求仍走 OAuth 路径，被路由到 `vip_2` 组，仍然 503。

### 方案二（有效）：同时设 `ANTHROPIC_AUTH_TOKEN` + `ANTHROPIC_BASE_URL`

在 VS Code 设置中注入 `ANTHROPIC_AUTH_TOKEN`，让扩展直接使用 API Key 认证，跳过 OAuth 流程，被路由到 `vip_1_max_enterprise` 组。

### 修改文件

`~/Library/Application Support/Code/User/settings.json`

### 修改内容

```json
{
  "claude-code.env": {
    "NO_PROXY": "127.0.0.1,localhost",
    "DISABLE_TELEMETRY": "1",
    "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  },
  "claudeCode.environmentVariables": [
    {
      "name": "NO_PROXY",
      "value": "127.0.0.1,localhost"
    },
    {
      "name": "DISABLE_TELEMETRY",
      "value": "1"
    },
    {
      "name": "ANTHROPIC_BASE_URL",
      "value": "https://api.deepseek.com/anthropic"
    },
    {
      "name": "ANTHROPIC_AUTH_TOKEN",
      "value": "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ]
}
```

### 注意事项

- 修改后需**退出 VS Code 完全重启**才能生效
- `ANTHROPIC_BASE_URL` 和 `ANTHROPIC_AUTH_TOKEN` 的值需与 `~/.claude/settings.json` 中的 `env` 字段保持一致
- **每次 `cc switch` 切换模型后**，如果 Key 或 Base URL 变了，需**手动同步更新 VS Code 设置**中的这两个变量
- 如嫌手动维护麻烦，可考虑找中转站开通一个 Key 通吃所有模型的方案

### 方案三（无效）：中转站一个 Key 通吃（方案 B）

在中转站后台尝试让一个 Key 同时覆盖贵价和便宜模型，免去手动同步。实测无效——中转站 `micuapi.ai` 本身不太稳定，贵价模型也偶尔不响应。

## 最终采用方案

**从终端 `code .` 启动 VS Code**（零维护方案）：

- 终端环境已被 `cc switch` 正确配置（API Key、Base URL、Model）
- 终端启动的 VS Code 继承终端环境变量，扩展直接可用
- `cc switch` 切换模型后无需手动同步任何设置
- 唯一代价：不能从 Dock/Launchpad 直接启动 VS Code

**备选**：如需桌面启动，使用方案二（在 VS Code 设置中加 `ANTHROPIC_AUTH_TOKEN`），但每次 `cc switch` 切换 Key/Base URL 后需手动同步。

## 验证结果

- [x] `ANTHROPIC_BASE_URL` 单独设置不足以解决问题
- [x] 加入 `ANTHROPIC_AUTH_TOKEN` 后，桌面启动 VS Code 便宜模型可正常使用
- [x] 中转站一个 Key 通吃方案无效（中转站本身不稳定）
- [x] 终端 `code .` 启动 VS Code 始终稳定可用
