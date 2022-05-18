def thesaurus(*args):
    namelist = list(map(str, args))                                                                         # ['Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева']
    dict_surnames = {}
    dict_main = {}
    for name in namelist:                                                                                   # Иван Сергеев
        surname = name.split(' ')[-1].title()                                                               # Сергеев
        first_letter_surname = surname[0]                                                                   # C
        dict_surnames[first_letter_surname] = dict_surnames.get(first_letter_surname, []) + [name]          # {'С': ['Иван Сергеев', 'Инна Серова', 'Анна Савельева'], 'А': ['Петр Алексеев'], 'И': ['Илья Иванов']}
    for namelist in dict_surnames.values():                                                                 # ['Иван Сергеев', 'Инна Серова', 'Анна Савельева']     ['Петр Алексеев']    ['Илья Иванов']
        dict_names = {}
        for name in namelist:                                                                               # Иван Сергеев
            surname = name.split(' ')[-1].title()                                                           # Сергеев
            first_letter_surname = surname[0]                                                               # C
            first_letter_name = name[0]                                                                     # И
            dict_names[first_letter_name] = sorted(dict_names.get(first_letter_name, []) + [name])          # {'И' : [Иван]}
            dict_main[first_letter_surname] = dict_main.get(first_letter_surname, dict_names)               # {'C' : {'И': ['Иван Сергеев']}
    return print(dict(sorted(dict_main.items())))                                                           # {'А': {'П': ['Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'С': {'И': ['Иван Сергеев', 'Инна Серова'], 'А': ['Анна Савельева']}}

thesaurus('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева')