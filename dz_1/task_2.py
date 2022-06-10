numbers = []

#a
numbers_summ = 0
for number in range(1, 1001, 2):
    number_in_cube = number**3
    number_cube_summ = 0
    while number_in_cube > 0:
        number_cube_summ += number_in_cube % 10
        number_in_cube = number_in_cube // 10
    if number_cube_summ % 7 == 0:
        numbers.append(number**3)
        numbers_summ += number**3                               # новая ветвь для суммы
print(numbers_summ)
#print(sum(numbers))


#b
new_numbers = []
new_numbers_summ = 0
for number in range(1, 1001, 2):
    number_in_cube = number ** 3 + 17
    number_cube_summ = 0
    while number_in_cube >= 1:
        number_cube_summ += number_in_cube % 10
        number_in_cube = number_in_cube // 10
    if number_cube_summ % 7 == 0:
        new_numbers.append(number ** 3)
        new_numbers_summ += number ** 3
#print(sum(new_numbers))
print(new_numbers_summ)
