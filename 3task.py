import random
i=1
pair=0#больше
first_pair=0#меньше
while i<=6:
    r1 = random.randint(1, 20)
    r2 = random.randint(1, 20)
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    if a > r1 and a > r2:
        pair+=1
    else:
        first_pair+=1
    if i==3:
        it7=r1
        it7=r2

if pair==first_pair:
    print("Случайные цифры в 7 итерации равны",)
else:
    p=(pair/first_pair*100)-100
print( "На" ,pair, "больше")






