from aiogram.types import BotCommand
from app.core.settings.config import get_settings, Settings
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

settings: Settings = get_settings()


async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Start bot."),
            BotCommand(command="help", description="Get help."),
        ]
    )


dp = Dispatcher()


async def get_bot() -> Bot:
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
    )
    await set_default_commands(bot)
    return bot
