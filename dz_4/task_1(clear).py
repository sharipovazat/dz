from requests import get
from decimal import Decimal

def currency_rates(char_code):
    responce = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    print(responce)
    currency_dict = {}
    for line in responce.split('</Value>'):
        parts_of_line = line.split('</CharCode')[0][-3:]
        currency_dict[parts_of_line] = line[-7:] if parts_of_line.isalpha() else print()

    char_code = char_code.upper()
    if currency_dict.setdefault(char_code) == None:
        print('Неверный код валюты')
    else:
        price = Decimal(currency_dict[char_code].replace(',', '.')).quantize(Decimal('0.01'))
        print(f'{char_code} = {price} руб.')

currency_rates(input('Введите код валюты: '))