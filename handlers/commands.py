from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.start import start_kb
from states import *


router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    print(message.from_user.username, 'start')
    await message.answer("Привет. Я бот, который будет лучшим поисковиком на маркетплейсах для тебя.\n"
                         "Выбери маркетплейс.", reply_markup=start_kb())
    await state.set_state(Position.start)
    await state.update_data({'sort_method': 'popular'})


async def start(message: Message, state: FSMContext):
    await message.answer("Привет. Я бот, который будет лучшим поисковиком на маркетплейсах для тебя.\n"
                         "Выбери маркетплейс.", reply_markup=start_kb())
    await state.set_state(Position.start)
