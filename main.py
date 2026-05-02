from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.core.star.star_handler import star_handlers_registry, EventType
from astrbot.core.star.filter.command import CommandFilter

from .translations import TRANSLATIONS, HIDDEN_CMDS, SUPPORTED_LANGS, UI_TEXT


@register("astrbot_plugin_i18n_help", "YourName", "让 /help 支持多语言切换", "1.0.0")
class I18nHelpPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def _get_lang(self) -> str:
        val = await self.get_kv_data("lang", None)
        return val if val in SUPPORTED_LANGS else "zh"

    def _build_help(self, lang: str) -> str:
        ui = UI_TEXT[lang]

        registered = set()
        for handler in star_handlers_registry:
            if handler.event_type != EventType.AdapterMessageEvent:
                continue
            for f in handler.event_filters:
                if isinstance(f, CommandFilter):
                    registered.add(f.command_name)

        lines = []
        for cmd, langs in TRANSLATIONS.items():
            if cmd not in registered or cmd in HIDDEN_CMDS:
                continue
            desc = langs.get(lang, langs.get("en", ""))
            lines.append(f"/{cmd:<16} {desc}")

        if not lines:
            return ui["no_cmds"]

        sep = "━━━━━━━━━━━━━━━━"
        return f"{ui['header']}\n{sep}\n" + "\n".join(lines) + f"\n{sep}\n{ui['footer']}"

    @filter.command("help", priority=10)
    async def help_cmd(self, event: AstrMessageEvent):
        """显示帮助信息 / Show help / Показать справку"""
        lang = await self._get_lang()
        yield event.plain_result(self._build_help(lang))
        event.stop_event()

    @filter.permission_type(filter.PermissionType.ADMIN)
    @filter.command("lang", priority=10)
    async def set_lang(self, event: AstrMessageEvent):
        """切换帮助语言 / Switch language / Переключить язык"""
        lang = await self._get_lang()
        ui = UI_TEXT[lang]
        args = event.message_str.strip().split()

        if len(args) < 2 or args[1] not in SUPPORTED_LANGS:
            supported = " / ".join(f"{k}({v})" for k, v in SUPPORTED_LANGS.items())
            yield event.plain_result(ui["lang_usage"] + supported)
            event.stop_event()
            return

        await self.put_kv_data("lang", args[1])
        new_ui = UI_TEXT[args[1]]
        yield event.plain_result(new_ui["lang_ok"] + SUPPORTED_LANGS[args[1]])
        event.stop_event()