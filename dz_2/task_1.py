print(15*3, type(15*3))                     # 45 <class 'int'>
print(15/3, type(15/3))                     # 5.0 <class 'float'>
print(15//3, type(15//3))                   # 5 <class 'int'>
print(15**3, type(15**3))                   # 3375 <class 'int'>


a_list = [15*3, 15/3, 15//3, 15**3]
my_map = list(map(type, a_list))
print(my_map)                               # [<class 'int'>, <class 'float'>, <class 'int'>, <class 'int'>]

print(*map(type, a_list))                   # <class 'int'> <class 'float'> <class 'int'> <class 'int'>