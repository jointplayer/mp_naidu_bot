from aiogram.types import FSInputFile

from states import Wildberries, ChosenMarketplace


def hl(a, b):
    return tuple([i for i in range(a, b + 1)])


hosts = {
    hl(0, 144): "basket-01.wbbasket.ru",
    hl(144, 288): "basket-02.wbbasket.ru",
    hl(288, 432): "basket-03.wbbasket.ru",
    hl(432, 720): "basket-04.wbbasket.ru",
    hl(720, 1008): "basket-05.wbbasket.ru",
    hl(1008, 1062): "basket-06.wbbasket.ru",
    hl(1062, 1116): "basket-07.wbbasket.ru",
    hl(1116, 1170): "basket-08.wbbasket.ru",
    hl(1170, 1314): "basket-09.wbbasket.ru",
    hl(1314, 1602): "basket-10.wbbasket.ru",
    hl(1602, 1656): "basket-11.wbbasket.ru",
    hl(1656, 1920): "basket-12.wbbasket.ru",
    hl(1920, 2046): "basket-13.wbbasket.ru",
    hl(2046, 2190): "basket-14.wbbasket.ru",
    hl(2190, 2400): "basket-15.wbbasket.ru",
    hl(2400, 2600): "basket-16.wbbasket.ru",
}

# --- test ---
'''
import requests
for i in range(2400, 2500):
    r = requests.get(f'https://basket-16.wbbasket.ru/vol{i}/part{i}00/{i}00223/images/c516x688/1.webp')
    if r.status_code != 200:
        print(i, r.status_code)
'''

back_destination = {
    'start': [Wildberries.is_chosen, ChosenMarketplace.ozon, ChosenMarketplace.megamarket],
    'wb_menu': [Wildberries.search],
    'wb_search': [Wildberries.slide_query, Wildberries.settings],
    'wb_settings': [Wildberries.sort_settings]
}

settings_banner = FSInputFile(r'media\img\settings_banner.png')
