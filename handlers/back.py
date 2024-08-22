# ⬅️ Назад

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from states import *
from handlers import commands
from handlers.search.wb import *
from utils.data import back_destination

router = Router()


async def back(message: Message, state: FSMContext, callback: CallbackQuery = None):
    current_state = await state.get_state()
    if current_state in back_destination['start']:
        await commands.start(message, state)
    elif current_state in back_destination['wb_menu']:
        await wb_menu(message, state)
    elif current_state in back_destination['wb_search']:
        await wb_search_after_settings(message, state)
    elif current_state in back_destination['wb_settings']:
        await wb_settings(callback, state)


@router.message(F.text == '⬅️ Назад')
async def keyboard_back(message: Message, state: FSMContext):
    await back(message, state)


@router.callback_query(F.data == 'back')
async def inline_back(callback: CallbackQuery, state: FSMContext):
    await back(callback.message, state, callback)
    await callback.answer()
