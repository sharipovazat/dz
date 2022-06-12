# Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import randint, choice

print(randint(0, 3))

a_list = ['один', 'два', 'три']
print(len(a_list))
rnd_nouns = randint(0, len(a_list)-1)
a_list.pop(rnd_nouns)
print(rnd_nouns)
print(a_list)

