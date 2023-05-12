from aiogram.fsm.state import State, StatesGroup

class Gen(StatesGroup):
    rand_image = State()
    self_image = State()
    text_prompt = State()
    link_prompt = State()