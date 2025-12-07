from aiogram import Router, types
from aiogram.filters import CommandStart, Command
import config
import sqlite3


profile_router = Router()
dbcon = sqlite3.connect(config.DB)
cursor = dbcon.cursor()


    

#@profile_router.message(Command("change_city"))
#async def change_city(message: types.Message):
