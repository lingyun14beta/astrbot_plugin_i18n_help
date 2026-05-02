# astrbot_plugin_i18n_help

> 如果 WebUI 提示指令冲突，可前往插件 → 管理行为，停用 AstrBot 自带的 `help` 指令；或每次重启后选择无视，不影响实际使用。

让 AstrBot 的 `/help` 指令支持多语言切换。

## 功能

- 替换原版 `/help`，输出当前语言的帮助信息
- 新增 `/lang` 指令切换语言，语言偏好永久保存
- 自动检测已安装的指令，`builtin_commands_extension` 未安装时其指令不会出现
- 只显示 AstrBot 自带指令和扩展插件指令，不显示其他第三方插件指令

## 支持的语言

| 代码 | 语言 |
|------|------|
| `zh` | 中文 |
| `en` | English |
| `ru` | Русский |

## 使用

发送 `/help` 查看帮助，默认语言为中文。

发送 `/lang zh`、`/lang en`、`/lang ru` 切换语言（仅管理员）。

## 注意

- 本插件优先级为 10，会覆盖原版 `/help`
- `builtin_commands_extension` 未安装时，其提供的指令不会出现在帮助列表中