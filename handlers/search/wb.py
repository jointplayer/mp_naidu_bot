import json
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, URLInputFile, InputMediaPhoto, FSInputFile

from search_engine.wb import get_data
from states import *
from filters import AlphabetCheck, NumberCheck
from keyboards.start import start_kb
from keyboards.wb import *
from utils.decorators import error_handler
from utils.data import settings_banner

router = Router()


async def wb_request(state, text, sort_method):
    query = get_data(text, sort_method)
    wb_query = str(query)
    max_slides = len(json.loads(query))
    await state.update_data({'wb_query': wb_query, 'max_slides': max_slides - 1})
    result = json.loads(wb_query)
    return result


def wb_formatter(query):
    art = query['art']
    name = query['name']
    brand = query['brand']
    brand_id = query['brand_id']
    price = query['price']
    s = (f"Артикул: <a href='https://www.wildberries.ru/catalog/{art}/detail.aspx'>{art}</a>\n"
         f"Название: {name}\n"
         f"Бренд: <a href='https://www.wildberries.ru/brands/{brand_id}'>{brand}</a>\n"
         f"Стоимость: {price} ₽")
    return s


@error_handler()
async def wb_search_after_settings(message: Message, state: FSMContext):
    data = await state.get_data()
    query = await wb_request(state, data['query'], data['sort_method'])
    data = await state.get_data()
    max_slides = data['max_slides']
    pic = query[0]['pic']
    await message.answer_photo(pic,
                               wb_formatter(query[0]),
                               reply_markup=wb_slider_kb(0, max_slides),
                               parse_mode='HTML')
    await state.set_state(Wildberries.search)


# ===== MESSAGES =====

@router.message(F.text == '🫐 Wildberries')
async def wb_menu(message: Message, state: FSMContext):
    await message.answer(
        "Введи свой запрос. Ищу на 🫐 Wildberries",
        reply_markup=back.button())
    await state.set_state(Wildberries.is_chosen)


@router.message(AlphabetCheck(), Wildberries.is_chosen)
@error_handler()
async def wb_search(message: Message, state: FSMContext):
    sort_method = (await state.get_data())['sort_method']
    query = await wb_request(state, message.text, sort_method)
    data = await state.get_data()
    await state.update_data({'query': message.text})
    max_slides = data['max_slides']
    pic = query[0]['pic']
    await message.answer_photo(pic,
                               wb_formatter(query[0]),
                               reply_markup=wb_slider_kb(0, max_slides),
                               parse_mode='HTML')
    await state.set_state(Wildberries.search)
    print(f'{message.from_user.username if message.from_user.username is not None
    else message.from_user.full_name} ищет "{message.text}" ')


@router.message(NumberCheck(), Wildberries.slide_query)
async def wb_slide_show(message: Message, state: FSMContext):
    slide = int(message.text) - 1
    data = await state.get_data()
    query = json.loads(data['wb_query'])
    max_slides = data['max_slides']
    if 0 < slide <= max_slides:
        pic = URLInputFile(query[slide]['pic'])
        await message.answer_photo(pic,
                                   caption=wb_formatter(query[slide]),
                                   parse_mode="HTML",
                                   reply_markup=wb_slider_kb(slide, max_slides))
        await state.set_state(Wildberries.slide)
    else:
        await message.answer('Неправильное значение. Введите другое.')


# ===== CALLBACKS =====

# sliders
@router.callback_query(F.data.startswith('slider_wb_'))
async def wb_slider(callback: CallbackQuery, state: FSMContext):
    slide = int(callback.data[10:])
    data = await state.get_data()
    query = json.loads(data['wb_query'])
    max_slides = data['max_slides']
    pic = URLInputFile(query[slide]['pic'])
    await callback.message.edit_media(InputMediaPhoto(media=pic,
                                                      caption=wb_formatter(query[slide]),
                                                      parse_mode="HTML"),
                                      reply_markup=wb_slider_kb(slide, max_slides))
    await callback.answer()


@router.callback_query(F.data == 'wb_slide')
async def wb_slide_wait(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    max_slides = data['max_slides'] + 1
    await callback.message.answer(f'Введите номер слайда (max: {max_slides})')
    await state.set_state(Wildberries.slide_query)


# settings
@router.callback_query(F.data == 'wb_settings')
async def wb_settings(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_media(InputMediaPhoto(media=settings_banner,
                                                      caption=f'Вы перешли в настройки поиска 🫐 Wildberries'),
                                      reply_markup=wb_settings_choice())
    await state.set_state(Wildberries.settings)


@router.callback_query(F.data == 'wb_settings_sort')
async def wb_sort_settings(callback: CallbackQuery, state: FSMContext):
    sort_method = (await state.get_data())['sort_method']
    await callback.message.edit_media(InputMediaPhoto(media=settings_banner,
                                                      caption=f'Вы перешли в настройки сортировки 🫐 Wildberries'),
                                      reply_markup=wb_sort_kb(sort_method))
    await state.set_state(Wildberries.sort_settings)


@router.callback_query(Wildberries.sort_settings)
async def wb_sort_pick(callback: CallbackQuery, state: FSMContext):
    await state.update_data({'sort_method': callback.data[3:]})
    await wb_search_after_settings(callback.message, state)
