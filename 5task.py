import random
a = int(input("Кол-во чисел: "))
d = [random.randint(1, 100) for i in range(a)]
print(d)
b=int(input("введите число,которое надо найти?"))
box=0
for i in d:
    for k in str(i):
        if int(k)==b:
           box=box+1

print(box)
# см фото доски


