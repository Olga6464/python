# 1.Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
def sal():
    try:
        time = float(input('Выработка в часах: '))
        salary = int(input('Ставка: '))
        bonus = int(input('Премия: '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника {res}')
    except ValueError:
        return print('Это не числовое значение')
sal()

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
my_list = [100, 4, 2, 1, 8, 6, 18]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

#3 Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
print(f'Числа от 20 до 240 кратные 20 и 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')


# 4.Представлен список чисел. Определить элементы списка, не имеющие повторений.
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) < 2 ]
print(my_new_list)

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
from functools import reduce


def my_func(el_p,el):
    return el_p * el
print(f'Список четных значений {[el for el in range(99,1001) if el % 2 == 0]}')
print(f'Результат произведения всех элелментов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

# 6. 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
from itertools import count

for el in count(int(input('Введите стартовое число'))):
    print(el) #приготовьтесь! бесконечный цикл
    break
from itertools import cycle

my_list = [True, 'QWE', 123, None]
for el in cycle(my_list):
    print(el) #бесконечный цикл
    break

#7.Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.


