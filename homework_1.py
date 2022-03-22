# Задание 1. Время

duration = input('Введите время в секундах: ')
min = 60
hour = min * 60
day = hour * 24


if int(duration) < min:
    print(duration, 'сек')
elif (int(duration) >= min) and (int(duration) <= hour):
    print(int(duration) // min, 'мин', int(duration) % min, 'сек')
elif (int(duration) >= hour) and (int(duration) <= day):
    print(int(duration) // hour, 'час', int(duration) % hour // min, 'мин', int(duration) % min, 'сек')
elif (int(duration) >= hour):
    print(int(duration) // day, 'дн', int(duration) % day // hour, 'час', int(duration) % day % hour // min, 'мин', int(duration) % day % hour % min, 'сек')


# Задание 2. Список кубов нечетных чисел от 1 до 1000
# Пункт А
cubes = []

for number in range(1000):
    if (number % 2 == 1):
        cube = number**3
        cubes.append(cube)

print(cubes)
summary = 0

for number in cubes:
    sum = 0
    num = number
    for k in range(1,len(str(number)) + 1):
        sum += num % 10
        num = num // 10

    if (sum % 7 == 0):
        summary += number
        print('Your summary is: ', summary, 'Your number is: ', number, 'Your sum is: ', sum)

# Пункты B и C

for number in cubes:
    sum = 0
    num = number + 17
    for k in range(1,len(str(number)) + 1):
        sum += num % 10
        num = num // 10
    if (sum % 7 == 0):
        summary += number
        print('Your summary is: ', summary, 'Your number is: ', number, 'Your sum is: ', sum)



# Задача 3. Склонение слова
percent = 'Процент'
for k in range(1,101):
    n = str(k)
    if (n[len(n) - 1] == '1') and (k not in range(5,21)):
        print(k, percent)
    elif k in range(5,21):
        print(k, percent + 'ов')
    elif (n[len(n) - 1] == '2') or (n[len(n) - 1] == '3') or (n[len(n) - 1] == '4'):
        print(k, percent + 'а')
    else:
        print(k, percent + 'ов')



