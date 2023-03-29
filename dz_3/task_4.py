# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }


def thesaurus(*args):
    #namelist = list(map(str, args))                                                                        # ['Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева']
    dict_main = {}
    dict_surnames = {}
    for name_surname in args:                                                                               # Иван Сергеев
        surname = name_surname.split(' ')[-1].title()                                                       # Сергеев
        first_letter_surname = surname[0]                                                                   # C
        dict_surnames[first_letter_surname] = dict_surnames.get(first_letter_surname, []) + [name_surname]  # {'С': ['Иван Сергеев', 'Инна Серова', 'Анна Савельева'], 'А': ['Петр Алексеев'], 'И': ['Илья Иванов']}
    print(dict_surnames)                                                                                    # {'С': ['Иван Сергеев', 'Инна Серова', 'Анна Савельева'], 'А': ['Петр Алексеев'], 'И': ['Илья Иванов']}
    for value in dict_surnames.values():                                                                    # ['Иван Сергеев', 'Инна Серова', 'Анна Савельева']     ['Петр Алексеев']    ['Илья Иванов']
        dict_names = {}
        for i in value:                                                                                     # Иван Сергеев
            surname = i.split(' ')[-1].title()                                                              # Сергеев
            first_letter_surname = surname[0]                                                               # C
            first_letter_name = i[0]                                                                        # И
            dict_names[first_letter_name] = dict_names.get(first_letter_name, []) + [i]                     # {'И' : [Иван Сергеев]}
            #dict_names[first_letter_name] = sorted(dict_names.get(first_letter_name, []) + [name_surname])
            dict_main[first_letter_surname] = dict_main.get(first_letter_surname, dict_names)               # {'C' : {'И': ['Иван Сергеев']}
    print("------------")
    print(dict_main)
    print(dict_main.get("С""И"))
    print("------------")
    return print(dict(sorted(dict_main.items())))                                                           # {'А': {'П': ['Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'С': {'И': ['Иван Сергеев', 'Инна Серова'], 'А': ['Анна Савельева']}}
    # return print(dict_main)                                                                               # {'С': {'И': ['Иван Сергеев', 'Инна Серова'], 'А': ['Анна Савельева']}, 'А': {'П': ['Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}}
thesaurus('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева')

