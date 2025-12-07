from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Погода на сегодня"), KeyboardButton(text="Погода на завтра")],
    [KeyboardButton(text="Сменить город")]
])