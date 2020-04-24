"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
from random import random

# загдываем число
R_NUMBER = int(random()*100)
print(R_NUMBER)
END = 10
i = 1

# отгадываем число
while True:
    if i <= END:
        print(f'попытка {i}')
        while True:
            try:
                USER_NUMBER = int(input('Введите число от 0 до 100\n'))
                break
            except ValueError:
                print('Вы вводите что-то не то попробуйте еще раз\n')
                i = i + 1
                print(f'попытка {i}')
        if R_NUMBER == USER_NUMBER:
            print("Вы угадали!!!")
            break
        elif R_NUMBER < USER_NUMBER:
            print("Ваше число больше загаднного\n")
            i = i + 1
        elif R_NUMBER > USER_NUMBER:
            print("Ваше меньше загаднного\n")
            i = i + 1
    else:
        print(f"Вы не угадали, число было {R_NUMBER}")
        break
