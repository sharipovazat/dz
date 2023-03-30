# Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice, randrange, randint

a_list = ['Ноль', 'Один', 'Два', 'Три']
print(choice(a_list))               # Два
print(randint(0, 3))                # 0, 1, 2, 3
print(randrange(0, 3))              # 0, 1, 2        (не включая последнее число)
print(randrange(0, 10, 3))          # 0, 3, 6, 9



# шутки повторяются, количество предложений 1
def get_jokes_1():
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    print(f'{choice(nouns).title()} {choice(adverbs)} {choice(adjectives)}')            # Лес завтра яркий


get_jokes_1()




# шутки повторяются, количество предложений выбирает пользователь
def get_jokes_x(x):                                                                       # Дом вчера мягкий

    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

    x = int(input('Введите количество шуток: '))                                        # Город сегодня яркий
    while x > 0:                                                                        # Лес завтра яркий
        print(choice(nouns).capitalize(), choice(adverbs), choice(adjectives))          # Огонь ночью веселый
        x -= 1                                                                          # Лес вчера веселый

get_jokes_x(2)






# шутки НЕ повторяются, метод randrange() количество предложений задано в аргументе функции
def get_jokes_randrange(x):

    nouns_1 = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs_1 = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives_1 = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

    while x > 0:
        random_ind_nouns = randrange(len(nouns_1))
        random_ind_adverbs = randrange(len(adverbs_1))
        random_ind_adjectives = randrange(len(adjectives_1))

        print(nouns_1[random_ind_nouns], adverbs_1[random_ind_adverbs], adjectives_1[random_ind_adjectives])
        nouns_1.remove(nouns_1[random_ind_nouns])
        adverbs_1.remove(adverbs_1[random_ind_adverbs])
        adjectives_1.remove(adjectives_1[random_ind_adjectives])
        x -= 1

get_jokes_randrange(3)





# шутки НЕ повторяются, метод choice(), количество шуток пользователь выбирает сам
def get_jokes_choice():
    question = int(input('Сколько шуток сгенерировать? '))
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    i = question
    while i > 0:
        choiced_nouns = choice(nouns)
        choiced_adverbs = choice(adverbs)
        choiced_adjectives = choice(adjectives)
        print(f'{choiced_nouns.title()} {choiced_adverbs} {choiced_adjectives}')            # Лес завтра яркий
        nouns.remove(choiced_nouns)
        adverbs.remove(choiced_adverbs)
        adjectives.remove(choiced_adjectives)
        i -= 1

get_jokes_choice()




# шутки НЕ повторяются, метод randint(), количество шуток пользователь выбирает сам
def get_jokes_randint():
    question = int(input('Сколько шуток сгенерировать? '))
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    i = question
    while i > 0:
        randint_nouns = randint(0, len(nouns)-1)
        randint_adverbs = randint(0, len(adverbs)-1)
        randint_adjectives = randint(0, len(adjectives)-1)
        print(f'{nouns[randint_nouns]} {adverbs[randint_adverbs]} {adjectives[randint_adjectives]}')            # лес позавчера мягкий
        nouns.pop(randint_nouns)                                                                                # дом ночью яркий
        adverbs.pop(randint_adverbs)                                                                            # город сегодня веселый
        adjectives.pop(randint_adjectives)
        i -= 1

get_jokes_randint()

