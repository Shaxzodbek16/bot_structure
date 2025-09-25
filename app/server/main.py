import logging
import sys
import asyncio
from aiogram import Dispatcher

from app.core.set_up import get_bot
from app.server.set_up import set_up_logs
from app.core.settings.config import get_settings, Settings

settings: Settings = get_settings()

dp = Dispatcher()


async def main() -> None:
    await set_up_logs()
    bot = await get_bot()
    # You can register your routers and middlewares here
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
