from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_btn_1 = InlineKeyboardButton("Рандомный фон", callback_data="bg_rand")
inline_btn_2 = InlineKeyboardButton("Загрузить свой фон", callback_data = "bg_upload")
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2)