from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton
import config

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Погода на сегодня"), KeyboardButton(text="Погода на завтра")],
    [KeyboardButton(text="Сменить город")]
])

def cities():
    buttons = []
    for city in config.CITIES.keys():
        buttons.append([KeyboardButton(text=city)])

    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True)