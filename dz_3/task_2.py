def num_translate_adv():
    numbers = input('Какое число нужно перевести на русский? ')
    eng_rus_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if numbers.istitle():
        return eng_rus_dict.get(numbers.lower()).title()
    else:
        return eng_rus_dict.get(numbers)

print(num_translate_adv())