
from curses.ascii import isalpha, isdigit
import random
play = range(1, 25)
computer = random.choice(play)
koll_popitok = 0

name = input('Здравствуйте! Как вас зовут?\n')
vibor1 = input("Вы хотите поиграть в угадай число?\nОтветьте пожалуйста да/нет: ")
vibor1 = ((str(vibor1)).lower())
if vibor1 == "да":
    print (f'Отлично, {name}, я загадала число между 1 и 25. Сможете угадать? У вас 5 попыток!')
    while koll_popitok < 5: 
        igrok = int(input('Введите число: '))
        koll_popitok += 1
        if igrok < computer:
            print ('Ваше число меньше того, что я загадала.')
        if igrok > computer:
            print ('Ваше число больще того, что я загадала.')
        if igrok == computer:
            break
    if igrok == computer:
        print (f'Вау, {name}! Вы угадали мое число, использовав {koll_popitok} попыток!')
        vibor2 = input("Хотите сыграть еще один раз?\nОтветьте пожалуйста да/нет: ")
        vibor2 = ((str(vibor2)).lower())
        if vibor2 == "нет":
            print("Игра закончена")
    else:
        print (f'К сожалению, вы не угадали мое число. Я загадала число {computer}')
else:
    print("Игра закончена")
