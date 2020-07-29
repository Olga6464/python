#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
from sys import argv

name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'Зрабаботная плата сотрудника {res}')
except ValueError:
    print('Это не числовое значение')


