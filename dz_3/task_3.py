names = ('Иван', 'Мария', 'Петр', 'Илья')
def thesaurus(names):
    names_dict = {}
    for name in names:
        first_letter_name = name[0]
        print(names_dict)
        if names_dict.get(first_letter_name):
            print('Уже есть такая буква')
            names_dict[first_letter_name] = name
        else:
            print('пока нет такой буквы', first_letter_name)
            names_dict[first_letter_name] = name
    return names_dict

print(thesaurus(names))