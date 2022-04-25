# Задание 1
import time

# Создаю класс
class TrafficLight:
    __color = "some color"

    def __init__(self, red, green, yellow):
        self.__red_color = red
        self.__green_color = green
        self.__yellow_color = yellow

    def running(self):
        print(self.__red_color)
        # time.sleep(7)
        print(self.__yellow_color)
        # time.sleep(2)
        print(self.__green_color)
        # time.sleep(10)
        print(self.__color)

a = TrafficLight("red", "green", "yellow")
a.running()

# Задание 2

class Road():

    def __init__(self, length, width, weight, high):
        self._length = length
        self._width = width
        print(self._width*self._length*weight*high)

a = Road(10,10,10,5)

# Задание 3

class Worker:
    name = "Max"
    surname = "Max's surname"
    position = "python-developer"
    _income = {"wage": 10000, "bonus": 1000}



class Position(Worker):

    def get_full_name(self):
        self.full_name = Worker.name + " " + Worker.surname
        return self.full_name

    def get_total_income(self):
        self.total_income = Worker._income["wage"] + Worker._income["bonus"]
        return self.total_income

    def __init__(self):
        print("Полное имя: ", self.get_full_name())
        print("Общий доход: ", self.get_total_income())


b = Position()
b.get_full_name()
b.get_total_income()

# Задание 4

class Car:
    speed = 0
    color = ""
    name = ""
    is_police = True

    def show_speed(self, your_speed, max_cars_speed):
        self.name = "Reno"
        self.speed = your_speed
        self.max_speed_town = max_cars_speed
        if self.speed < self.max_speed_town:
            return self.speed
        else:
            return f"Превышение скорости, максимальная скорость {self.max_speed_town}"

    def go(self):
        return print("Машина поехала")

    def stop(self):
        return print("Машина остановилась")

    def turn(self):
        return print("Машина повернула")


class TownCar(Car):
    pass

class SportCar:
    pass

class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass


car = Car()
towncar = TownCar()
workcar = WorkCar()
print("Городская машина:", towncar.show_speed(23, 60), towncar.go())
print("Рабочая машина:", workcar.show_speed(90, 40), workcar.turn())

# Задание 5
class Stationery:
    title = ""

    def draw(self, massage):
        print("Запуск отрисовки " + massage)

class Pen(Stationery):
    def __init__(self, massage):
        super().draw(massage)

class Pencil(Stationery):
    def __init__(self, massage):
        super().draw(massage)

class Handle(Stationery):
    def __init__(self, massage):
        super().draw(massage)

pen = Pen("ручкой")
pencin = Pencil("карандашом")
handle = Handle("маркером")




