from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from kb.reply import r_zap

from fsm.fsm import Reg

user = Router()


@user.message(CommandStart())
async def start(mes: Message):
    await mes.answer('Привет, я бот для записи тебя на всякую хуету, нажми на кнопку чтобы записаться',
                     reply_markup=r_zap)


@user.message(F.text == 'Записаться')
async def zap(mes: Message):
    pass


@user.message(F.text == 'не записываться')
async def no_zap(mes: Message):
    await mes.answer('Да пошел ты нахуй')