names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
         'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']

for name_profession in names:
    only_name = name_profession.split(' ')[-1].capitalize()
    print(f'Привет, {only_name}!')
