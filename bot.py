from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import keyboard
import generator

TOKEN = "" # your bot's token
PROJECT_PATH = "/home/arseniy/quotesGenerator" # replace this path with your local

bot = Bot(TOKEN)
dp = Dispatcher(bot)

#initial dialog
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Я помогу сделать картинку с цитатой. Какую ты хочешь?", reply_markup=keyboard.inline_kb1)

@dp.callback_query_handler(lambda c: c.data)
async def process_callback_rand(callback_query: types.CallbackQuery):
    code = callback_query.data
    if code == "bg_rand":
        await bot.send_message(callback_query.from_user.id, "Напиши цитату")
        
        imagePath = generator.genImage()
        image = open(f'{PROJECT_PATH}/{imagePath}', 'rb')
        await bot.send_photo(callback_query.from_user.id, image)

    elif code == "bg_upload":
        await bot.send_message(callback_query.from_user.id, "Загрузи картинку")
    else:
        await bot.answer_callback_query(callback_query.id, "Произошла ошибка")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('Вот что я умею:\n1) Генерировать картинки со случайным фоном\n2) Генерировать картинки с заданным фоном')

@dp.message_handler()
async def error_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Я не понял команду(')

if __name__ == '__main__':
    executor.start_polling(dp)