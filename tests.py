a_dict = {
     "А": {"П": ["Петр Алексеев"]},
     "И": {"И": ["Илья Иванов"]},
     "С": {"И": ["Иван Сергеев", "Инна Серова"],
           "А": ["Анна Савельева"]}
}

# sur: {'И': ['Иван Сергеев', 'Инна Серова', 'Илья Иванов'], 'П': ['Петр Алексеев'], 'А': ['Анна Савельева']}
def thesaurus(*args):
    dict_names = {}
    dict_surnames = {}
    for i in args:
        name, surname = i.split()
        first_letter_name = name[0]
        dict_names[first_letter_name] = dict_names.get(first_letter_name, []) + [i]
    for k, v in dict_names.items():
        for i in v:
            name, surname = i.split()
            first_letter_surname = surname[0]
            dict_surnames[first_letter_surname] = dict_surnames.get(first_letter_surname, [])   # {'С': [], 'И': [], 'А': []}
        dict_surnames['C'] = dict_surnames.get('C', []) + [k,v]
    print(dict_surnames)
        #dict_surnames[first_letter_surname] =
    print('sur:', dict_names)
thesaurus('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева')



"""


def thesaurus_2(*args):
    surnames_dict = {}
    names_dict = {}
    for name_surname in args:
        name, surname = name_surname.split()
        first_letter_name = name[0]
        names_dict[first_letter_name] = names_dict.get(first_letter_name, []) + [name_surname]
    for k, v in names_dict.items():                     # 'И': ['Иван Игнеев', 'Илья Ивлев']
        for i in v:                                     # Иван Сергеев
            name, surname = i.split()                   # name = Иван      surname = Игнеев
            first_letter_surname = surname[0]           # first_letter_surname = И
            surnames_dict[first_letter_surname] = surnames_dict.get(first_letter_surname, []) + [k,v]   # 'И' = 'И': ['Иван Игнеев', 'Илья Ивлев']




    print('surnames_dict:', surnames_dict)
    return names_dict


print(thesaurus_2('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева'))
"""
"""
listok = ['Axxxx Pxxxx', 'Txxxx Pxxxx']
dict_p = {}

dict_p = dict_p['a'] = 'Axxxx Pxxxx'
dict_p = dict_p['t'] = 'Txxxx Pxxxx'

all_dict = {
    'A': ['Axxxx Pxxxx'],
    'T': ['Txxxx Pxxxx'],
    'B': ['Bxxxx Vxxxx'],
    'C': ['Cxxxx Rxxxx', 'Cxxxx Kxxxx']
}

P = {
    'A': ['Axxxx Pxxxx'],
    'T': ['Txxxx Pxxxx']
}

V = {
    'B': ['Bxxxx Vxxxx']
}

R = {
    'C': ['Cxxxx Rxxxx']
}
"""

