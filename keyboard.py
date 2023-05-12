#from aiogram.types import ReplyKeyboardRemove, \
#    ReplyKeyboardMarkup, KeyboardButton, \
#    InlineKeyboardMarkup, InlineKeyboardButton
#
#inline_btn_1 = InlineKeyboardButton("Рандомный фон", callback_data="bg_rand")
#inline_btn_2 = InlineKeyboardButton("Загрузить свой фон", callback_data = "bg_upload")
#inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2)

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="📝 Своё изображение", callback_data="set_image"),
    InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])