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

"""
time = int(input("Enter the time in seconds: "))

days = time // 86400
hour = time % 86400 // 3600
minutes = time % 86400 % 3600 // 60
sec = time % 86400 % 3600 % 60

if days > 0:
    print(days, "days", end=" ")
if hour > 0:
    print(hour, "hours", end=" ")
if minutes > 0:
    print(minutes, "min", end=" ")
if sec > 0:
    print(sec, "sec")
"""

# 1000000 -> 11 дн 13 час 46 мин 40 сек
# 10000000 -> 115 дн 17 час 46 мин 40 сек