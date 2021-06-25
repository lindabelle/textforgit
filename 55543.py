

import random

i = 1
bol = 0
n_bol = 0
while i <= 6:
    print("Проверка №", i)
    r1 = random.randint(1, 20)
    r2 = random.randint(1, 20)
    # print('Рандомные', r1, r2)
    a = int(input("Введите число в промежутке от 1 до 20: "))
    b = int(input("Введите число в промежутке от 1 до 20: "))

    if a > r1 and a > r2:
        bol += 1
    else:
        n_bol += 1

    if i == 3:

        it_3_1 = r1
        it_3_2 = r2
    i += 1

if bol == n_bol:
    print('Случайные числа в 3 итерации равны', it_3_1, it_3_2)
else:
    p = (bol / n_bol * 100) - 100
    print("На", bol, "% больше")