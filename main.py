import asyncio
from aiogram import Bot, Dispatcher
from bot.config import API_TOKEN
from bot.database.models import init_db
from bot.handlers import start, profile, match, payments

async def main():
    await init_db()
    bot = Bot(API_TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        start.router,
        profile.router,
        match.router,
        payments.router,
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
