import asyncio
import os

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from aiogram import Dispatcher, Bot

from handlers.user import user


bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()

dp.include_router(user)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)

asyncio.run(main())