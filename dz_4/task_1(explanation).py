#import requests               # можно сразу весь requests импортировать
from requests import get       # импортируем из requests функция fet
from decimal import Decimal    # из модуля округления decimal импортируем класс Decimal(как float и int только Decimal). Можно с int, с float нет

#---------------------------------------------------------------------------------------------------------------------
# 1 БЛОК (получаем ответ от сервера, обрабатываем его, создаем словарь со значениями и ключами
#---------------------------------------------------------------------------------------------------------------------
link = 'http://www.cbr.ru/scripts/XML_daily.asp'                                   # берём ссылку
responce = get(link).text                                                          # для удобства присваеваем в переменную с функцией get и методом text для получения Инфы с сервера и дальше начинаем её уже обрабатывать
#print(requests.get(link).text)                                                    # <?xml version="1.0" encoding="windows-1251"?><ValCurs Date="08.04.2023" name=
#encodings = utils.get_encoding_from_headers(responce.headers)
#content = responce.content.decode(encoding=encodings)

currency_dict = {}                                                                  # создаём пустой словарь
# ищем код валюты и её значение
for line in responce.split('</Value>'):                                             # перебираем весь текст и делим на отрезки по '</Value>'
    #print(line)                                                                     # </Valute><Valute ID="R01020A"><NumCode>944</NumCode><CharCode>AZN</CharCode><Nominal>1</Nominal><Name>Азербайджанский манат</Name><Value>45,3417
    #part_of_line = line.split('</CharCode')                                        # отрезок делим еще на отрезки по '</CharCode' (получаем две строки в списке)
    #print(part_of_line)                                                            # ['</Valute><Valute ID="R01020A"><NumCode>944</NumCode><CharCode>AZN', '><Nominal>1</Nominal><Name>Азербайджанский манат</Name><Value>45,3417']
    parts_of_line = line.split('</CharCode')[0][-3:]                                 # сделали то же самое, но еще сразу из первого отрезка забрали три поледних элемента
    #print(parts_of_line)                                                             # AZN (это код валюты). НАШЛИ!
    currency_dict[parts_of_line] = line[-7:] if parts_of_line.isalpha() else print()  # в созданный ранее словарь добавляем по ключу (код валюты) добавляем значение сразу, без отдельной переменной. Получим список с валютой и её стоимостью
    # словарь  [ключ(КОД ВАЛЮТЫ)]=последние 7 цифр ЕСЛИ код валюты.БУКВЫ ЕСЛИ НЕТ печатаем пустоту
#print(currency_dict)                                                                 # {'AUD': '57,2403', 'AZN': '45,3417', 'GBP': '00,1281', 'AMD': '16,4278', 'BYN': '27,8774', 'BGN': '42,5767', 'BRL': '16,5193', 'HUF': '22,5165'...

#---------------------------------------------------------------------------------------------------------------------
# 2 БЛОК (То, что вводит пользователь сопоставляем со словарем из 1 блока и выводим Инфу
#---------------------------------------------------------------------------------------------------------------------
# Аргумент для def currency_rates(сюда)
def currency_rates(char_code):

    char_code = char_code.upper()                                                              # переводим все символы в верхний регистр ааа >>> AAA
    if currency_dict.setdefault(char_code) == None:                                            # ЕСЛИ значения нет в словаре,то оно добавялется со значением None и выводится на экран 'Неверный код валюты'
        print('Неверный код валюты')
    else:                                                                                      # Если оно есть, то выводим ключ от пользователя и соответсвующее ему отформатированное значение в словаре
        price = Decimal(currency_dict[char_code].replace(',', '.')).quantize(Decimal('0.01'))  # Объекты Decimal имеют метод quantize(), который позволяет округлять числа. Используемая строка "0.01" указывает, что округление будет идти до 1 знака в дробной части.
        # переменная = класс(ключ словаря, введенный пользователем.МЕНЯЕМ , на . .ОКРУГЛЯЕМ('до двух точек после запятой')
        print(f'{char_code} = {price} руб.')

    #print(currency_dict)

currency_rates(input('Введите код валюты: '))                                                   #вызываем функцию currency_rates(аргумент вводит пользователь - код валюты)


