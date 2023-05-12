from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


import asyncio
import logging

from handlers import router

TOKEN = "6040903928:AAEy4D2Qj8CTRoUNnzwoblMbh8W7cdyoVG0" # your bot's token

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True) # delete all updates(messages, etc.), created while inactivity
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())




#initial dialog
#@dp.message_handler(commands=['start'])
#async def start_command(message: types.Message):
#    await message.reply("Привет! Я помогу сделать картинку с цитатой. Какую ты хочешь?", reply_markup=keyboard.inline_kb1)
#
#@dp.callback_query_handler(lambda c: c.data)
#async def process_callback_rand(callback_query: types.CallbackQuery):
#    code = callback_query.data
#    if code == "bg_rand":
#        await bot.send_message(callback_query.from_user.id, "Напиши цитату")
#        
#        imagePath = generator.genImage()
#        image = open(f'{PROJECT_PATH}/{imagePath}', 'rb')
#        await bot.send_photo(callback_query.from_user.id, image)
#
#    elif code == "bg_upload":
#        await bot.send_message(callback_query.from_user.id, "Загрузи картинку")
#    else:
#        await bot.answer_callback_query(callback_query.id, "Произошла ошибка")
#
#@dp.message_handler(commands=['help'])
#async def help_command(message: types.Message):
#    await message.reply('Вот что я умею:\n1) Генерировать картинки со случайным фоном\n2) Генерировать картинки с заданным фоном')
#
#@dp.message_handler()
#async def error_message(message: types.Message):
#    await bot.send_message(message.from_user.id, 'Я не понял команду(')
#
#if __name__ == '__main__':
#    executor.start_polling(dp)