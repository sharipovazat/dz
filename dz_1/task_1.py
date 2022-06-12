duration = int(input('Введите секунды: '))

days = duration // 86400
hours = duration % 86400 // 3600
minuts = (duration - (days * 86400 + hours * 3600)) // 60
secunds = (duration - (days * 86400 + hours * 3600 + minuts * 60))

if days > 0:
    print(f'{days} дн', end=' ')
if hours > 0:
    print(f'{hours} час', end=' ')
if minuts > 0:
    print(f'{minuts} мин', end=' ')
if secunds > 0:
    print(f'{secunds} сек', end=' ')

# 1000000 -> 11 дн 13 час 46 мин 40 сек
# 10000000 -> 115 дн 17 час 46 мин 40 сек