from random import choice, randrange


def get_jokes(x):
    """
    x = int(input('Введите количество шуток: '))
    если нужно чтобы пользователь вводил сам число нужных шуток
    """

    while x > 0:
        print(choice(nouns), choice(adverbs), choice(adjectives))
        x -= 1

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

get_jokes(2)

print()
print('НЕПОВТОРЯЮЩИЕСЯ ШУТКИ:')
print()


def new_get_jokes(x):
    while x > 0:
        random_ind_nouns = randrange(len(nouns_1))
        random_ind_adverbs = randrange(len(adverbs_1))
        random_ind_adjectives = randrange(len(adjectives_1))
        print(nouns_1[random_ind_nouns], adverbs_1[random_ind_adverbs], adjectives_1[random_ind_adjectives])
        nouns_1.remove(nouns_1[random_ind_nouns])
        adverbs_1.remove(adverbs_1[random_ind_adverbs])
        adjectives_1.remove(adjectives_1[random_ind_adjectives])
        x -= 1

nouns_1 = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs_1 = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives_1 = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

new_get_jokes(5)


