# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))

# num = "husd#hgieolf#he;ye#wih"
# print(num.split('#'))
# print(num.replace("e", "*"))

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = input("Введите действие: ")

# if num3 == "+":
#     print(f"Ответ: {num1 + num2}")
# elif num3 == "-":
#     print(f"Ответ: {num1 - num2}")
# elif num3 == "*":
#     print(f"Ответ: {num1 * num2}")
# elif num3 == "/":
#     print(f"Ответ: {num1 / num2}")
   

# a = 1
# b = 2
# c = 3
# a,b,c = c,a,b
# print(a,b,c)

# stroka = "Love"
# print(stroka[-1])
# print(stroka[-2:])
# print(stroka[::-1])
# print(len(stroka))




# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}

# for key, val in a.items():
#     # if val / 5:
#     #     a.update(b)
#     new_val = val / 5
#     a.update({key: new_val})

# print(a)

# 1) Напишите программу, которая запрашивает с ввода семь чисел через запятую, добавляет их в список. На экран выводит первое и последнее число списка. Затем удаляет последнее число и вместо него вставляет слово “Makers”.
# Например: 
# Ввод: Введите цифры через запятую: 5, 7, 8, 1, 3, 0, 8
# Вывод: 5 8
# [5, 7, 8, 1, 3, 0, ‘Makers’]
# """

# num1 = input("Введите 7 цифр через запятую: ").split(", ")
# num2 = []
# for number in num1:
#     num2.append(int(number))

# print(num2[0], num2[-1])

# # num2.pop()
# # num2.appened("Makers")
# num2[-1] = "Makers"

# print(num2)

# name_of_list = 'Helloworld!'
# name_of_list2 = list('Helloworld!')
# print(name_of_list2)

# Создайте список list_, состоящий ровно из двух строк.
# Переставьте эти строки местами.
# Результат запишите в новый список new_list и выведите в консоль получившийся результат
# Например, если list_ выглядит так:

# ['world', 'hello'] 
# результат будет:
# ['hello', 'world'] 

# num1 = input("Введите цифры через запятую: ").split(",")
# list_ = []
# for number in num1:
#     list_.append(int(number))

# print[(str(list_))]

# num1 = (input()).split(",")
# list_ = []
# for number in num1:
#     list_.append(int(number))
#     list_.sort()

# print(list_)

# num1 = (str(input())).split(",")
# list_ = []
# for number in num1:
#     list_.append(int(number))


# print(sorted(list_))
# list_ = [1, 1, 3]

# for i in range(10):
#     if list_.count(i) == 2:
#         print("yes")
#     elif list_.count(i) == 3:
#         print("yes")
#     elif list_.count(i) > 2:
#         print("ERROR")

# list_ = [[i for i in range(1,4)]]* 3
# # list_2 = [list_] * 3
# print(list_)

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# # a = {
# #     key: 
# #     for key, val in dict_.items()
# # }

# # print(dict_)

# for key, val in dict_.items():
#     if val % 2 == 0:
#         dict_[key] = str('even')
#     else:
#         dict_[key] = str("odd")

# print(dict_)


string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
string_2 = string_.split()
print(string_2)