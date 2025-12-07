from aiogram import Router, types
from aiogram.filters import CommandStart
from services import user_service
import keyboards

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    id = message.from_user.id
    await message.answer(text="Hello world", reply_markup=keyboards.main)
    await user_service.try_add_new_user(id)

    print("USER_ID = " + str(message.from_user.id))