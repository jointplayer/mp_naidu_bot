from aiogram.fsm.state import StatesGroup, State


class Position(StatesGroup):
    start = State()


class ChosenMarketplace(StatesGroup):
    ozon = State()
    megamarket = State()


class Wildberries(StatesGroup):
    is_chosen = State()
    search = State()
    slide = State()
    slide_query = State()
    settings = State()
    sort_settings = State()
