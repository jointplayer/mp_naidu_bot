from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text="🫐 Wildberries"))
    kb.add(types.KeyboardButton(text="💨 OZON"))
    kb.add(types.KeyboardButton(text="✅ Мегамаркет"))
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)