TRANSLATIONS: dict[str, dict[str, str]] = {
    # === 核心内置命令 ===
    # 来源：AstrBot 主程序 builtin_commands
    "help": {
        "zh": "显示帮助",
        "en": "Show help",
        "ru": "Показать справку",
    },
    "new": {
        "zh": "新建对话",
        "en": "Create new conversation",
        "ru": "Создать новый диалог",
    },
    "reset": {
        "zh": "重置对话历史",
        "en": "Reset conversation history",
        "ru": "Сбросить историю диалога",
    },
    "sid": {
        "zh": "获取会话 ID 及相关信息",
        "en": "Get session ID and other related information",
        "ru": "Получить ID сессии и связанную информацию",
    },
    "stats": {
        "zh": "显示当前对话的 token 用量统计",
        "en": "Show token usage statistics for the current conversation",
        "ru": "Показать статистику использования токенов в диалоге",
    },
    "stop": {
        "zh": "停止 Agent 执行",
        "en": "Stop agent execution",
        "ru": "Остановить выполнение агента",
    },

    # === builtin_commands_extension 插件 ===
    # 来源：https://github.com/AstrBotDevs/builtin_commands_extension
    "llm": {
        "zh": "开启或关闭 LLM 聊天功能",
        "en": "Enable or disable LLM chat",
        "ru": "Включить или отключить чат с LLM",
    },
    "plugin": {
        "zh": "插件管理",
        "en": "Plugin management",
        "ru": "Управление плагинами",
    },
    "op": {
        "zh": "授权管理员",
        "en": "Grant admin privileges",
        "ru": "Назначить администратора",
    },
    "deop": {
        "zh": "取消管理员授权",
        "en": "Revoke admin privileges",
        "ru": "Снять администратора",
    },
    "provider": {
        "zh": "查看或切换 LLM 提供商",
        "en": "View or switch LLM provider",
        "ru": "Просмотр или смена провайдера LLM",
    },
    "model": {
        "zh": "查看或切换模型",
        "en": "View or switch model",
        "ru": "Просмотр или смена модели",
    },
    "history": {
        "zh": "查看对话记录",
        "en": "View conversation history",
        "ru": "Просмотр истории диалога",
    },
    "ls": {
        "zh": "查看对话列表",
        "en": "List conversations",
        "ru": "Список диалогов",
    },
    "groupnew": {
        "zh": "创建群聊对话",
        "en": "Create group conversation",
        "ru": "Создать групповой диалог",
    },
    "switch": {
        "zh": "切换对话",
        "en": "Switch conversation",
        "ru": "Переключить диалог",
    },
    "rename": {
        "zh": "重命名当前对话",
        "en": "Rename current conversation",
        "ru": "Переименовать текущий диалог",
    },
    "del": {
        "zh": "删除当前对话",
        "en": "Delete current conversation",
        "ru": "Удалить текущий диалог",
    },
    "persona": {
        "zh": "查看或切换 Persona",
        "en": "View or switch persona",
        "ru": "Просмотр или смена персоны",
    },
    "set": {
        "zh": "设置会话变量",
        "en": "Set session variable",
        "ru": "Установить переменную сессии",
    },
    "unset": {
        "zh": "移除会话变量",
        "en": "Remove session variable",
        "ru": "Удалить переменную сессии",
    },

    # === 本插件自身 ===
    "lang": {
        "zh": "切换帮助语言（zh / en / ru）",
        "en": "Switch help language (zh / en / ru)",
        "ru": "Переключить язык справки (zh / en / ru)",
    },
}

# 支持的语言列表（用于 /lang 参数校验和提示）
SUPPORTED_LANGS: dict[str, str] = {
    "zh": "中文",
    "en": "English",
    "ru": "Русский",
}

# 不在帮助中展示的内部命令
HIDDEN_CMDS: set[str] = {
    "dashboard_update",
}

# 各语言的 UI 文本
UI_TEXT: dict[str, dict[str, str]] = {
    "zh": {
        "header":     "📖 AstrBot 帮助",
        "footer":     "💡 发送消息即可与 AI 对话",
        "no_cmds":    "（暂无可用指令）",
        "lang_usage": "用法：/lang <语言代码>\n支持：",
        "lang_ok":    "✅ 已切换语言：",
    },
    "en": {
        "header":     "📖 AstrBot Help",
        "footer":     "💡 Just send a message to chat with AI",
        "no_cmds":    "(No commands available)",
        "lang_usage": "Usage: /lang <code>\nSupported: ",
        "lang_ok":    "✅ Language switched to: ",
    },
    "ru": {
        "header":     "📖 Справка AstrBot",
        "footer":     "💡 Просто отправьте сообщение, чтобы пообщаться с ИИ",
        "no_cmds":    "(Нет доступных команд)",
        "lang_usage": "Использование: /lang <код>\nПоддерживается: ",
        "lang_ok":    "✅ Язык переключён на: ",
    },
}