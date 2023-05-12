from aiogram import Bot, types, Router, F, Dispatcher, flags
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.handlers import callback_query

from states import Gen
import keyboard
import text
import generator

PROJECT_PATH = "/home/arseniy/quotesGenerator" # replace this path with your local
router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup = keyboard.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=keyboard.menu)



#@router.callback_query(F.data == 'generate_text')
#async def input_text_prompt(clbck: callback_query, state: FSMContext):
#    await state.set_state(Gen.text_prompt)
#    await clbck.message.edit_text(text.gen_text)
#    await clbck.message.answer(text.gen_exit, reply_markup=keyboard.exit_kb)

# Random image option handler
@router.callback_query(F.data == 'generate_image')
async def input_image_prompt(clbck: callback_query, state: FSMContext):
    await state.set_state(Gen.rand_image)
    #await clbck.message.edit_text(text.gen_random)
    #await clbck.message.answer(text.gen_exit, reply_markup=keyboard.exit_kb)

@router.message(Gen.rand_image)
@flags.chat_action("upload_photo")
async def generate_image(msg: Message, state: FSMContext):
    # genImage will return path to the image
    mesg = await msg.answer(text.gen_wait)
    imagePath = generator.genImage()
    img_result = open('/home/arseniy/quotesGenetrator/output/05-05-2023_18-28-42.png', 'rb')
    await mesg.answer_photo(photo=img_result)