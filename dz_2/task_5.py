coast = [43, 54.5, 342.54, 985, 985.05, 3223, 234, 433.4, 23, 202.3, 23, 43.64, 43.4, 2232, 1, 3.4]

#a
for element in coast:
    cops = element * 100 % 100
    print(f'{int(element)} руб {int(cops):02d} коп')

print(id(coast))



#b
print()
print('ЗАДАНИЕ В')
print()

coast.sort()
for element in coast:
    cops = element * 100 % 100
    print(f'{int(element)} руб {int(cops):02d} коп')

print(id(coast))

#C
print()
print('ЗАДАНИЕ C')
print()

new_coast = sorted(coast, reverse=True)
for element in new_coast:
    cops = element * 100 % 100
    print(f'{int(element)} руб {int(cops):02d} коп')

print(id(new_coast), id(coast))

#D
print()
print('ЗАДАНИЕ D')
print()

coast.sort()
for element in coast[-5:]:
    cops = element * 100 % 100
    print(f'{int(element)} руб {int(cops):02d} коп')