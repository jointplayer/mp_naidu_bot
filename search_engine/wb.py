import requests
import json
from utils.data import hosts


def get_host(value):
    for key in hosts.keys():
        if key[0] <= value < key[-1]:
            return hosts[key]
    return None


def get_data(query, sort_method):
    r = requests.get(f'https://search.wb.ru/exactmatch/ru/common/v7/search?'
                     f'ab_testid=newlogscore'
                     f'&appType=1'
                     f'&curr=rub'
                     f'&dest=-1067582'
                     f'&query={query}'
                     f'&resultset=catalog'
                     f'&sort={sort_method}'
                     f'&spp=30'
                     f'&suppressSpellcheck=false')
    json_dict = json.loads(r.text)
    products = json_dict['data']['products']
    result = []
    for i in range(0, len(products)):
        item = {}
        art = products[i]['id']
        name = products[i]['name']
        brand = products[i]['brand']
        brand_id = products[i]['brandId']
        price = products[i]['sizes'][0]['price']['product'] // 100
        vol = int(art // 1e5)
        part = int(art // 1e3)
        host = get_host(vol)
        pic = fr'https://{host}/vol{vol}/part{part}/{art}/images/big/1.webp'
        item['art'] = art
        item['name'] = name
        item['brand'] = brand
        item['pic'] = pic
        item['brand_id'] = brand_id
        item['price'] = price
        result.append(item)
    return json.dumps(result, ensure_ascii=False)
