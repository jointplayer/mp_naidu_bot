from functools import wraps
from aiogram import types

from keyboards.start import start_kb


def error_handler():
    def decorator(func):
        @wraps(func)
        async def wrapper(message: types.Message, *args, **kwargs):
            for i in range(10):
                try:
                    return await func(message, *args, **kwargs)
                except Exception as e:
                    print(f'{message.from_user.username}: ошибка: {e}')
            else:
                await message.answer(
                    f'Произошла ошибка. Напишите /start и попробуйте ещё раз или обратитесь к администратору '
                    f'@jointplayer',
                    reply_markup=start_kb())
        return wrapper
    return decorator
