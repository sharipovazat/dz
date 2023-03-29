# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
#>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
#{
#    "И": ["Иван", "Илья"],
#    "М": ["Мария"], "П": ["Петр"]
#}

# аргумента нет
def thesaurus():
    names = ('Иван', 'Мария', 'Петр', 'Илья')
    names_dict = {}
    for name in names:
        names_dict[name[0]] = names_dict.get(name[0], []) + [name]
    return names_dict
print(thesaurus())


# аргумент *args
def thesaurus_args(*args):
    dict_names = {}
    for name in args:
        first_letter = name[0]
        dict_names[first_letter] = dict_names.get(first_letter, []) + [name]
    return dict_names
print(thesaurus_args('Иван', 'Мария', 'Антон', 'Илья'))


# И -> [] + [Иван]
# М -> [] + [Мария]
# А -> [] + [Антон]
# И -> [Иван] + [Илья]