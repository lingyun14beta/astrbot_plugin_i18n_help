import aiohttp

from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star
from astrbot.core.config.default import VERSION
from astrbot.core.star.star import star_map
from astrbot.core.star.star_handler import star_handlers_registry, EventType
from astrbot.core.star.filter.command import CommandFilter

try:
    from astrbot.core.dashboard_assets import get_dashboard_version
    HAS_DASHBOARD_VERSION = True
except ImportError:
    try:
        from astrbot.core.utils.io import get_dashboard_version
        HAS_DASHBOARD_VERSION = True
    except ImportError:
        HAS_DASHBOARD_VERSION = False

from .translations import TRANSLATIONS, HIDDEN_CMDS, SUPPORTED_LANGS, UI_TEXT


class I18nHelpPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def _get_lang(self) -> str:
        val = await self.get_kv_data("lang", None)
        return val if val in SUPPORTED_LANGS else "zh"

    async def _query_notice(self) -> str:
        try:
            async with aiohttp.ClientSession(trust_env=True) as session:
                async with session.get("https://astrbot.app/notice.json", timeout=2) as resp:
                    return (await resp.json())["notice"]
        except BaseException:
            return ""

    async def _build_help(self, lang: str) -> str:
        ui = UI_TEXT[lang]

        registered = set()
        for handler in star_handlers_registry:
            if handler.event_type != EventType.AdapterMessageEvent:
                continue
            plugin = star_map.get(handler.handler_module_path)
            if plugin and not plugin.activated:
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
        body = f"{ui['header']}\n{sep}\n" + "\n".join(lines) + f"\n{sep}\n{ui['footer']}"

        if HAS_DASHBOARD_VERSION:
            try:
                dashboard_version = await get_dashboard_version()
            except BaseException:
                dashboard_version = None
        else:
            dashboard_version = None
        dashboard_line = f"(WebUI: {dashboard_version})" if dashboard_version else ""
        version_line = f"AstrBot v{VERSION}{dashboard_line}"
        notice = await self._query_notice()
        msg = f"{version_line}\n\n{body}"
        if notice:
            msg += f"\n\n{notice}"
        return msg

    @filter.command("help", priority=2)
    async def help_cmd(self, event: AstrMessageEvent):
        """显示帮助信息 / Show help / Показать справку"""
        lang = await self._get_lang()
        yield event.plain_result(await self._build_help(lang))
        event.stop_event()

    @filter.permission_type(filter.PermissionType.ADMIN)
    @filter.command("lang", priority=2)
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
