def thesaurus():
    names = ('Иван', 'Мария', 'Петр', 'Илья')
    names_dict = {}
    for name in names:
        names_dict[name[0]] = names_dict.get(name[0], []) + [name]
        #print(names_dict)
    return names_dict

print(thesaurus())
