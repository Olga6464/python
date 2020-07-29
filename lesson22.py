#1.Создать список и заполнить его элементами различных типов данных.
n_list = [None, 27, -18, 44.5, 'Max', True, False]
def n_type(elem):
    for elem in range(len(n_list)):
        print(type(n_list[elem]))

n_type(n_list)

# 2.Для списка реализовать обмен значений соседних элементов..

list_item =input('Введите элементы списка, через пробел: ').split()
i = 0
for i in range(0,len(list_item) -1,2):
    list_item[i], list_item[i + 1] = list_item[i + 1],list_item[i]
print(list_item)

#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
seasons_dict = {'Зима': (1,2,12),
                'Весна': (3,4,5),
                'Лето': (6,7,8),
                'Осень': (9,10,11)}
months = int (input('Введите месяц в виде целого числа: '))
for key in seasons_dict.keys():
    if months in seasons_dict[key]:
        print(key)
seasons_list = ['Winter', 'Spring','Summer', 'Autumn']
if months == 1 or months == 2 or months == 12:
    print('Winter')
elif months == 3 or months == 3 or months == 5:
    print('Spring')
elif months == 6 or months == 7 or months == 8:
    print('Summer')
elif months == 9 or months == 10 or months == 11:
    print('Autumn')
else:
    print('Honeymoon over')

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
my_str = input("Введите фрзу: ")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1

#5.Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (111 - выход) "))
while digit != 111:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число "))