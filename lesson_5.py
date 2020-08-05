# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных
# свидетельствует пустая строка.

my_f = open('text.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('text.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()

# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов
# в каждой строке.

my_file = open('text2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('text2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('text2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1}  в строке {len(content[1])}')
my_file = open('text2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и
# величину их окладов. Определить, кто из
# сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text3.txt', 'r') as my_file:
   workers = {}
   for i in my_file:
      key, value = i.split()
      workers[key] = value
      if int(value) < 20000:
         print(f'{key}: Зарплата меньше 20 000')
# print(f'Средний оклад {sum(map{key}) / len{key}}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на
# чтение и считывающую построчно данные.
# При этом английские числительные должны
# заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text4.txt', 'r') as file_obj:

    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('text4_1.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить
# ее на экран.

def summsry():
    try:
        with open('text5.txt', 'w+') as f:
            line = input('Введите цифры через пробел \n')
            f.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода')
summsry()

# 6. Необходимо создать (не программно) текстовый
# файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и
# лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий.
# Сформировать словарь, содержащий название
# предмета и общее количество занятий по нему.
# Вывести словарь на экран.

import json
data = {
        'income':
            {
                 'Informatics' : 170,
                'Physics' : 40,
               'Sports' : 30
             }
}
with open('my_file.json', 'w') as f:
    json.dump(data, f)
with open('my_file.json') as f:
    data = json.load(f)





