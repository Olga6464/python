#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
def div(*args):

    try:
        arg_1 = int(input('Введите делитель'))
        arg_2 = int(input('Введите делимое'))
        result = arg_1 / arg_2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return 'На ноль делить нельзя'

    return result
print(f'result {div()}')

#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.

def persona(**kwargs):
    return kwargs

print(persona(
    name=input('Введите имя: '),
    surname=input('Введите фамилию: '),
    date=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('Электронный адрес: '),
    tel=input('Номер телефона: '),
))
#3  Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func (a,b,c):
   try:
       my_list = [a,b,c]
       my_list.pop(my_list.index(min(my_list)))
       return sum(my_list)
   except TypeError:
       return 'Номер'

print(my_func(5,6,7))

#4 Программа принимает действительное положительное число x и целое отрицательное число y.
def my_pow_func(x,y):
    try:
        ans = x ** y
    except TypeError:
        return 'Не целое число'
    return  ans

print(my_pow_func(18, -4))

#
def my_pow_func(x,y):
    try:
        x,y = float(x), int(y)
        result = x
        for i in range(abs(y) - 1):
            result *= x
        return 1 / result
    except ValueError:
        return 'Check value'

print(my_pow_func(2, -2))

#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
def summ():
    z = False
    result = 0
    while z == False:
        numbers = input('Ведите номер или w для выхода: ').split()
        res_line = 0
        for num in numbers:
            if 'w' in num:
                z = True
                break
            res_line += int(num)
        result += res_line
    print(result)
 # 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
def  int_func(*args):
    word = input('Введите слово')
    print(word.title())
    return
int_func()






