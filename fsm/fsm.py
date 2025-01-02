from aiogram.fsm.state import State, StatesGroup

class Reg(StatesGroup):
    name = State()
    number = State()
    time = State()