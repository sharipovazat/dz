#b (in place)
# Дано
start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Нужно ->>> ['в', '"05"', 'часов', '"17"', 'минут', 'температура', 'воздуха', 'была', '"+05"', 'градусов']
# 1 СПОСОБ
print(start_list)                                           # ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
x = 0
for i in start_list:
    if i[0] in ["+", "-"]:
        start_list[x] = f'"{i[0]}{int(i[1:]):02d}"'
    elif i.isdigit():
        start_list[x] = f'"{int(i):02d}"'
    else:
        start_list[x] = i
    x += 1
print(start_list)                                           # ['в', '"05"', 'часов', '"17"', 'минут', 'температура', 'воздуха', 'была', '"+05"', 'градусов']

# 2 СПОСОБ
start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for index, element in enumerate(start_list):
    if element.isdigit():
        start_list[index] = f'"{int(element):02d}"'
    elif element[1:].isdigit():
        start_list[index] = f'"{element[0]}{int(element):02d}"'
print(start_list)                                           # ['в', '"05"', 'часов', '"17"', 'минут', 'температура', 'воздуха', 'была', '"+05"', 'градусов']


# СФОРМИРОВАТЬ ИЗ ОБРАБОТАННОГО СПИСкА СТРОКУ ->>> в "05" часов "17" минут температура воздуха была "+05" градусов
print(' '.join(start_list))                                 # в "05" часов "17" минут температура воздуха была "+05" градусов



# 2.1
# Дано
start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Нужно ->>> ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
new_list = []
for i in start_list:
    if i[0] in ["+", "-"]:
        if i[1].isdigit():
            new_i = f'{i[0]}{int(i[1:]):02d}'
            new_list.extend(['"', new_i, '"'])
    elif i.isdigit():
        new_i = f'{int(i):02d}'
        new_list.extend(['"', new_i, '"'])
    else:
        new_list.append(i)
print(new_list)                                                     # ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']



# 1 СПОСОБ (in place)
x = 0
for i in start_list:
    if i[0] in ["+", "-"]:
        start_list[x] = f'"{i[0]}{int(i[1:]):02d}"'
    elif i.isdigit():
        start_list[x] = f'"{int(i):02d}"'
    else:
        start_list[x] = i
    x += 1
print(start_list)                                                   # ['в', '"05"', 'часов', '"17"', 'минут', 'температура', 'воздуха', 'была', '"+05"', 'градусов']

# 2 СПОСОБ (in place)
start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(start_list):
    element = start_list[i]                                         # элемент равен объекту по индексу в списке
    if element[0] in ['+', '-']:                                    # если первый символ у элемента + или -, то:
        start_list[i] = f'{element[0]}{int(element[1:]):02d}'       # элемент по индексу в списке = + или - и сам элемент без первого символа с двумя целыми числами
        start_list.insert(i+1, '"')
        start_list.insert(i, '"')
        i += 1                                                      # сдвиг из-за кавычки
    else:
        if element.isnumeric():
            start_list[i] = f'{int(element):02d}'
            start_list.insert(i+1, '"')
            start_list.insert(i, '"')
            i += 1                                                  # сдвиг из-за кавычки
    i += 1                                                          # сдвиг по циклу
print(start_list)                                                   # ['в', '"', '05', '"', 'часов', '"', '-17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']



