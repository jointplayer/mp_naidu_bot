from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import *
from keyboards.wb import *

router = Router()


@router.message(F.text == '💨 OZON')
async def ozon_menu(message: Message, state: FSMContext):
    await message.answer("Ты нажал OZON.", reply_markup=back.button())
    await state.set_state(ChosenMarketplace.ozon)


@router.message(F.text == '✅ Мегамаркет', Position.start)
async def megamarket_menu(message: Message, state: FSMContext):
    await message.answer("Ты нажал мегамаркет.", reply_markup=back.button())
    await state.set_state(ChosenMarketplace.megamarket)
