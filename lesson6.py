#1. Создать класс TrafficLight (светофор) и определить
# у него один атрибут color (цвет) и метод running
# (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора
# в режимы: красный, желтый, зеленый. Продолжительность
# первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами
# должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу
# примера, создав экземпляр и вызвав описанный  метод.

from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый','Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n'
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()

# 2. Реализовать класс Road (дорога), в котором
# определить атрибуты: length (длина), width
# (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в
# 1 см * чи сло см толщины полотна. Проверить
# работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return  self._length * self._width

class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume

r = MassCount(25, 1000, 125)
print(r.mass())

# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний
# атрибут должен быть защищенным и ссылаться на
# словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе
# класса Worker. В классе Position реализовать
# методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера
# на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return  self.name + ' ' + self.surname

    def get_total_income(self):
        return  self._income.get('wage') + self._income.get('bonus')

a = Position('Max','Born','Agent007', 5000, 200)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

# 5. Реализовать класс Stationery (канцелярская
# принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом
# из классов реализовать переопределение метода
# draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать
# экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())









