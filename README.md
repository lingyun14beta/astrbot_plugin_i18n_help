# astrbot_plugin_i18n_help

> 如果 WebUI 提示指令冲突，可前往插件 → 管理行为，停用 AstrBot 自带的 `help` 指令；或每次重启后选择无视，不影响实际使用。
>
> If the WebUI warns about a command conflict, go to Plugins → Manage Behaviors and disable AstrBot's built-in `help` command, or simply dismiss the warning on each restart — it does not affect normal usage.
>
> Если WebUI сообщает о конфликте команд, перейдите в Плагины → Управление поведением и отключите встроенную команду `help` в AstrBot, или просто игнорируйте предупреждение при каждом перезапуске — это не влияет на работу.

让 AstrBot 的 `/help` 指令支持多语言切换。

Adds multi-language support to AstrBot's `/help` command.

Добавляет поддержку нескольких языков в команду `/help` AstrBot.

---

## 功能 / Features / Функции

- 替换原版 `/help`，输出当前语言的帮助信息
- 新增 `/lang` 指令切换语言，语言偏好永久保存
- 自动检测已安装的指令，`builtin_commands_extension` 未安装时其指令不会出现
- 只显示 AstrBot 自带指令和扩展插件指令，不显示其他第三方插件指令

---

- Replaces the default `/help` with localized output
- Adds `/lang` command to switch language; preference is saved permanently
- Auto-detects installed commands — commands from `builtin_commands_extension` are hidden if the plugin is not installed
- Only shows AstrBot built-in and extension plugin commands, not arbitrary third-party plugin commands

---

- Заменяет стандартный `/help` на вывод на текущем языке
- Добавляет команду `/lang` для переключения языка; выбор сохраняется навсегда
- Автоматически определяет установленные команды — команды `builtin_commands_extension` скрыты, если плагин не установлен
- Отображает только встроенные команды AstrBot и команды плагинов расширений, но не сторонних плагинов

---

## 支持的语言 / Supported Languages / Поддерживаемые языки

| 代码 / Code / Код | 语言 / Language / Язык |
|---|---|
| `zh` | 中文 |
| `en` | English |
| `ru` | Русский |

---

## 使用 / Usage / Использование

发送 `/help` 查看帮助，默认语言为中文。发送 `/lang zh`、`/lang en`、`/lang ru` 切换语言（仅管理员）。

Send `/help` to view help. Default language is Chinese. Send `/lang zh`, `/lang en`, or `/lang ru` to switch language (admin only).

Отправьте `/help` для просмотра справки. Язык по умолчанию — китайский. Отправьте `/lang zh`, `/lang en` или `/lang ru` для переключения языка (только для администраторов).

---

## 注意 / Notes / Примечания

- 本插件优先级为 2，会覆盖原版 `/help`
- `builtin_commands_extension` 未安装时，其提供的指令不会出现在帮助列表中

---

- This plugin has priority 2 and overrides the default `/help`
- If `builtin_commands_extension` is not installed, its commands will not appear in the help list

---

- Этот плагин имеет приоритет 2 и переопределяет стандартный `/help`
- Если `builtin_commands_extension` не установлен, его команды не будут отображаться в списке справки
