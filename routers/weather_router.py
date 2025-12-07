from aiogram import Router, types, F
from aiogram.filters import Command
from services import weather_service, user_service

weather_router = Router()

@weather_router.message(F.text == "Погода на сегодня")
async def get_weather(message: types.Message):
    city = await user_service.get_city(message.from_user.id)
    weather = await weather_service.get_weather_for_city(city)
    await message.answer(weather)

@weather_router.message(F.text == "Погода на завтра")
async def get_weather(message: types.Message):
    city = await user_service.get_city(message.from_user.id)
    weather = await weather_service.get_weather_for_city(city, day_offset=2)
    await message.answer(weather)