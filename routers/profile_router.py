from aiogram import Router, F, types
from services import user_service
import keyboards
import config


profile_router = Router()

@profile_router.message(F.text == "Сменить город")
async def change_city(message: types.Message):
    await message.answer(text="Смена города", reply_markup=keyboards.cities())

@profile_router.message(F.text.in_(list(config.CITIES.keys())))
async def change_city(message: types.Message):
    await user_service.change_city(message.from_user.id, message.text)
    await message.answer(text="Город успешно сменён на " + message.text + " ✅", reply_markup=keyboards.main)