# Задание 2. Валюта
from requests import utils, get
import requests
from bs4 import BeautifulSoup
import xml.dom.minidom
import utils

http = 'http://www.cbr.ru/scripts/XML_daily.asp'

#def get_content(URL):
#    soup = BeautifulSoup(URL, 'html.parser')
#    items = soup.find_all('div', class_ = 'line')
#    print(items)
#    cars =[]
#    for item in items:
#        cars.append({
#            'title': item.find('div', class_ = 'line').get_text(strip = True)
#        })
# get_text(strip = True) получает текст и обрезает концевые пробелы

# Этот метод если мы испольхуем html, с http так не работает




def current_rates(http):
    site = get(http)
    if site.status_code == 200: # Проверка, достучались ли мы до сайта
        not_parsed = site.text # Получаем строчку, которую нельзя парсить
        not_parsed = xml.dom.minidom.parseString(not_parsed) #Приводим перменную к виду виртуальной таблицы для парсинга
        # с помощью элемента имя_элемента.getElementsByTagName
        date = not_parsed.getElementsByTagName("ValCurs")[0]
        date = f"Текущий курс ЦБ на {date.getAttribute('Date')}"
        print(date)

        node_array = not_parsed.getElementsByTagName("Valute") # Получаем словарь элементов

        your_valute = input("Введите вашую валюту: ")

        for your_number in node_array:
            valute_name = your_number.getElementsByTagName("Name")[0]

            valute_name = valute_name.childNodes[0].nodeValue

            value = your_number.getElementsByTagName("Value")[0]
            # так как value это тег, получать его значение будем следующим образом
            value = value.childNodes[0].nodeValue

            code = your_number.getElementsByTagName("CharCode")[0]
            code = code.childNodes[0].nodeValue

            if code == str(your_valute):
                print(date, ':', value, 'руб', valute_name)
    else:
        print('Error')
    return None






# Задание 3 Импорт собственного модуля


utils.current_rates(http)











