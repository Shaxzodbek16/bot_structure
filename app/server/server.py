import asyncio

from aiogram import Bot, Dispatcher

from app.core.settings.config import get_settings


async def main() -> None:
    settings = get_settings()
    bot = Bot(settings.BOT_TOKEN)
    dp = Dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
