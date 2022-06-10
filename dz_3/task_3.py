def thesaurus():
    names = ('Иван', 'Мария', 'Петр', 'Илья')
    names_dict = {}
    for name in names:
        names_dict[name[0]] = names_dict.get(name[0], []) + [name]
    return names_dict

print(thesaurus())


def thesaurus_args(*args):
    dict_names = {}
    for i in args:
        first_letter = i[0]
        dict_names[first_letter] = dict_names.get(first_letter, []) + [i]
    return dict_names


print(thesaurus_args('Иван', 'Мария', 'Антон', 'Илья'))


# И -> [] + [Иван]
# М -> [] + [Мария]
# А -> [] + [Антон]
# И -> [Иван] + [Илья]