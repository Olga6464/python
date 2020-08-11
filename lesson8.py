# 2. Создайте собственный класс-исключение, обрабатывающий
# ситуацию деления на нуль. Проверьте его работу на
# данных, вводимых пользователем. При вводе пользователем
# нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))


# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте
# работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)

# 3. Создайте собственный класс-исключение, который должен
# проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять
# список. Класс-исключение должен контролировать типы
# данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы
# запрашиваются бесконечно, пока пользователь сам не
# остановит работу скрипта, введя, например, команду
# “stop”. При этом скрипт завершается, сформированный
# список выводится на экран.

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):


        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

try_except = Error(1)
print(try_except.my_input())





# 1. Реализовать класс «Дата», функция-конструктор
# которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два
# метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '_': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return  f'Все правильно'
                else:
                    return f'Неправильный год'
            else:
                return  f'Неправильный месяц'
        else:
            return  f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'

today = Data('11, 1, 2001')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract('11, 11, 2011'))
print(today.extract('11, 11, 2021'))
print(Data.valid(1, 11, 2000))





