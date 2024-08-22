import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import commands, back, menu
from handlers.search import wb

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(back.router,
                       commands.router,
                       menu.router,
                       wb.router)

    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
