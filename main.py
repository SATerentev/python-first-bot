from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))