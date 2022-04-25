# 1. Выяснить тип результата

print(type(15*5))
print(type(15/5))
print(type(15//5))
print(type(15**5))

# 2. из списка в строку

mas = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
massage = ''
print(type(mas[2]))
a = '"'
for k in mas:
    if k.isdigit() == True and len(k) < 2:
        k = '"' + '0' + k + '"'
    if k.isdigit():
        k = '"' + k + '"'

    if k[0] in '+-' and len(k) <= 2:
        index = k.find('+-')
        k = a + k[:1] + '0' +k[1:] + a
    massage = massage + k + ' '
print(massage)

# 4. Список должностей

post = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for n in post:
    n = n[::-1]
    n = n.split(' ')
    n = n[0][::-1]
    n = n.lower()
    n = n.capitalize()
    greeting = f'Привет, {n}'
    print(greeting)


# 5. Список цен
import random
prices = []
price_now = []
print(type(prices))
# A
for q in range(21):
    price = random.random() * 1000
    price_now.append(price)
    for i in range(len(price_now) - 1):
        for j in range(len(price_now) - i - 1):
            if price_now[j] > price_now[j + 1]:
                price_now[j], price_now[j + 1] = price_now[j + 1], price_now[j]



    price = ('{:.2f}').format(price)
    price_parts = price.split('.')
    print(price_parts)
    cost = price_parts[0] + ' руб. ' + price_parts[1] + ' коп.'
    prices.append(cost)
print(prices)

# B

print(price_now)
print(type(price_now[0]))
