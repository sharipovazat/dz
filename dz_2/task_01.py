print(15*3, type(15*3))
print(15/3, type(15/3))
print(15//3, type(15//3))
print(15**3, type(15**3))


a_list = [15*3, 15/3, 15//3, 15**3]
my_map = list(map(type, a_list))
print(my_map)

print(*map(type, a_list))