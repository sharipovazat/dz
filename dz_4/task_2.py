import requests
from requests import get, utils
from decimal import Decimal

link = 'http://www.cbr.ru/scripts/XML_daily.asp'
print(requests.get(link).text)

def currency_rates(char_code):
    link = 'http://www.cbr.ru/scripts/XML_daily.asp'
    responce = get(link).text
    #encodings = utils.get_encoding_from_headers(responce.headers)
    #content = responce.content.decode(encoding=encodings)

    currency_dict = {}
    for n in responce.split('</Value>'): # находим код валюты и её значение
        i = n.split('</CharCode')[0][-3:]
        currency_dict[i] = n[-7:] if i.isalpha() else print()   # создаем список с валютой и её стоимостью

    char_code = char_code.upper()
    if currency_dict.setdefault(char_code) == None:
        print('Неверный код валюты')
    else:
        price = Decimal(currency_dict[char_code].replace(',', '.')).quantize(Decimal('0.01'))
        print(f'{char_code} = {price} руб.')

currency_rates(input('Введите код валюты: '))
#print(currency_rates())