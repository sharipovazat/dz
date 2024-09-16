from requests import get
from decimal import Decimal

def currency_rates(char_code):
    zapros = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    print(zapros)
    kurs_valut_slovar = {}
    for line in zapros.split('</Value>'):
        parts_of_line = line.split('</CharCode')[0][-3:]
        kurs_valut_slovar [parts_of_line] = line[-7:] if parts_of_line.isalpha() else print()
    char_code = char_code.upper()
    if kurs_valut_slovar .setdefault(char_code) == None:
        print('Неверный код валюты')
    else:
        price = Decimal(kurs_valut_slovar[char_code].replace(',', '.')).quantize(Decimal('0.01'))
        print(f'{char_code} = {price} руб.')

currency_rates(input('Введите код валюты: '))