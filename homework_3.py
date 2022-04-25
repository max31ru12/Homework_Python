# 1 и 2. Перевод числительных от 0 до 10
from random import randint



En = ['zero', 'one', 'two', 'Three', 'Four', 'five', 'six', 'seven', 'Eight', 'nine', 'ten']
Rus = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']


def num_translate(En, Rus, str_num):

    for k in range(0,len(En)):
        En[k] = En[k].capitalize()
        Rus[k] = Rus[k].capitalize()



    if str_num not in En:
        return print(None)
    else:
        id = En.index(str_num)
        return print(Rus[id])


num_translate(En, Rus, input('Введите число на англиской языке: '))

# 3. Имена и списки




