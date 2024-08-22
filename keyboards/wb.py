from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards import back

wb = {
    'popular': ['wb_popular', 'по популярности'],
    'rate': ['wb_rate', 'по рейтингу'],
    'priceup': ['wb_priceup', "по возрастанию цены ▲"],
    'pricedown': ['wb_pricedown', "по убыванию цены ▼"],
    'newly': ['wb_newly', "по новинкам"],
    'benefit': ['wb_benefit', "сначала выгодные"]
}


def wb_sort_kb(picked_method) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    wb[picked_method][1] = '☑ ' + wb[picked_method][1]
    kb.row(types.InlineKeyboardButton(
        text=wb['popular'][1], callback_data=wb['popular'][0])
    )
    kb.row(types.InlineKeyboardButton(
        text=wb['rate'][1], callback_data=wb['rate'][0])
    )
    kb.row(types.InlineKeyboardButton(
        text=wb['priceup'][1], callback_data=wb['priceup'][0])
    )
    kb.row(types.InlineKeyboardButton(
        text=wb['pricedown'][1], callback_data=wb['pricedown'][0])
    )
    kb.row(types.InlineKeyboardButton(
        text=wb['newly'][1], callback_data=wb['newly'][0])
    )
    kb.row(types.InlineKeyboardButton(
        text=wb['benefit'][1], callback_data=wb['benefit'][0])
    )
    back.inline_button(kb)
    wb[picked_method][1] = wb[picked_method][1][2:]
    return kb.as_markup(resize_keyboard=True)


def wb_slider_kb(slide, max_slides) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    if slide == 0:
        kb.row(InlineKeyboardButton(text=f'>>',
                                    callback_data=f'slider_wb_{slide + 1}'))
    elif slide == max_slides:
        kb.row(InlineKeyboardButton(text=f'<<',
                                    callback_data=f'slider_wb_{slide - 1}'))
    else:
        kb.row(InlineKeyboardButton(text=f'<<',
                                    callback_data=f'slider_wb_{slide - 1}'),
               InlineKeyboardButton(text=f'>>',
                                    callback_data=f'slider_wb_{slide + 1}'
                                    ))
    kb.row(InlineKeyboardButton(text=f'{slide + 1}/{max_slides + 1}',
                                callback_data='wb_slide'))
    kb.row(InlineKeyboardButton(text=f'⚙️ настройки',
                                callback_data='wb_settings'))
    kb.row(InlineKeyboardButton(text=f'⬅️ назад',
                                callback_data=f'back'))
    return kb.as_markup(resize_keyboard=True)


def wb_settings_choice() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text='сортировка',
                                callback_data='wb_settings_sort'))
    kb.row(InlineKeyboardButton(text=f'фильтры (soon)',
                                callback_data='wb_settings_filters'))
    kb.row(InlineKeyboardButton(text=f'⬅️ назад',
                                callback_data=f'back'))
    return kb.as_markup(resize_keyboard=True)
