a_dict = {
     "А": {"П": ["Петр Алексеев"]},
     "И": {"И": ["Илья Иванов"]},
     "С": {"И": ["Иван Сергеев", "Инна Серова"],
           "А": ["Анна Савельева"]}
}

def thesaurus(*args):
    #namelist = list(map(str, args))                                                                        # ['Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева']
    dict_surnames = {}
    dict_main = {}
    for name in args:                                                                                       # Иван Сергеев
        surname = name.split(' ')[-1].title()                                                               # Сергеев
        first_letter_surname = surname[0]                                                                   # C
        dict_surnames[first_letter_surname] = dict_surnames.get(first_letter_surname, []) + [name]          # {'С': ['Иван Сергеев', 'Инна Серова', 'Анна Савельева'], 'А': ['Петр Алексеев'], 'И': ['Илья Иванов']}
    print(dict_surnames)
    for value in dict_surnames.values():                                                                    # ['Иван Сергеев', 'Инна Серова', 'Анна Савельева']     ['Петр Алексеев']    ['Илья Иванов']
        dict_names = {}
        for name_surname in value:                                                                          # Иван Сергеев
            surname = name_surname.split(' ')[-1].title()                                                   # Сергеев
            first_letter_surname = surname[0]                                                               # C
            first_letter_name = name_surname[0]                                                             # И
            dict_names[first_letter_name] = dict_names.get(first_letter_name, []) + [name_surname]          # {'И' : [Иван Сергеев]}
            #dict_names[first_letter_name] = sorted(dict_names.get(first_letter_name, []) + [name_surname])
            dict_main[first_letter_surname] = dict_main.get(first_letter_surname, dict_names)               # {'C' : {'И': ['Иван Сергеев']}
    return print(dict(sorted(dict_main.items())))                                                           # {'А': {'П': ['Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'С': {'И': ['Иван Сергеев', 'Инна Серова'], 'А': ['Анна Савельева']}}
    # return print(dict_main)                                                                               # {'С': {'И': ['Иван Сергеев', 'Инна Серова'], 'А': ['Анна Савельева']}, 'А': {'П': ['Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}}
thesaurus('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева')