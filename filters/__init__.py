import regex

from aiogram.filters import BaseFilter
from aiogram import types


class AlphabetCheck(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return regex.fullmatch(r'^[\p{L}\s\d]+$', message.text) is not None


class NumberCheck(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return regex.fullmatch(r'^\d+$', message.text) is not None