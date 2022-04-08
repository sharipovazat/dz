for i in range(1, 101):
    if 10 <= i <= 14:
        print(i, 'процентов')
    #if i == 1 or i == 21 or i == 31 or i == 41 or i == 41 or i == 51 or i == 61 or i == 71 or i == 81 or i == 91:
    elif i % 10 == 1:
        print(i, 'процент')
    #elif 2 <= i <= 4 or 22 <= i <= 24 or 32 <= i <= 34 or 42 <= i <= 44 or 52 <= i <= 54 or 62 <= i <= 64 or 72 <= i <= 74 or 82 <= i <= 84 or 92 <= i <= 94:
    #elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
    elif i % 10 in [2, 3, 4]:
        print(i, 'процента')
    else:
        print(i, 'процентов')






