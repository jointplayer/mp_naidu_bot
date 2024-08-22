from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def button() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.add(types.KeyboardButton(text="⬅️ Назад"))
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def inline_button(kb):
    kb.row(types.InlineKeyboardButton(
        text="назад", callback_data='back')
    )
    return kb
