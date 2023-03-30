# 2.1
# Дано
start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Нужно ->>> ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

for ind, val in enumerate(start_list):
    if val.isdigit() and int(val) < 10:                            # Для значения нужно проверить сначала цифра ли это, потом еще и преобразовать в int()
        start_list[ind] = f'{int(val):02d}'
    elif val[0].isdigit() or val[-1].isdigit():
        start_list[ind] = f'{val[0]}{int(val[1:]):02d}'
print(start_list)