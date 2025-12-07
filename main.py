from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import BOT_TOKEN
from routers.weather_router import weather_router
from routers.profile_router import profile_router
from routers.start_router import start_router
import asyncio

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(weather_router)
    dp.include_router(profile_router)
    dp.include_router(start_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())