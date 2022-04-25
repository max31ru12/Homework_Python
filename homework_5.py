# Задание 1. Генерация нечетных чисел от одного до n
from itertools import islice
from random import randint

n = randint(1,10)
print(n)

def num_generation(n):

    for num in range(1, n + 1, 2):
        yield num




print(*islice(num_generation(n), n))

# Задание 3. List Comprehensions для двух списков

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Helen', 'Max'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

if len(tutors) > len(klasses):
    k = len(tutors) - len(klasses)
    for n in range(k):
        klasses.append('None')

    result_list = [
        i for i in zip(tutors, klasses)
    ]

print(result_list) # Это не генератор, тут и доказывать нечего

# Задание 4. Вывод элементов, которые больше предыдущего

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [
    n for i, n in enumerate(src[1:], start=1) if n > src[i-1]
]

print(result)
# enumerate возвращает кортеж, первый элемент кортежа - индекс элемента из src
# второй элемент кортежа - значение элемента с данным индексом

# Задание 5. Элементы списка, не имеющие повторений

scr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [
    n for n in scr if scr.count(n) == 1
]

print(result)


