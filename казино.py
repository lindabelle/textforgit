import random
n=random.randint(1,10)
c1=input("Введите цвет: ")#red=1
c2=input("Введите цвет: ")#black=2
for i in range(n):
    if i==1 and c2:
        print("Верно")
        i+=1
    elif i==3 and c1:
        print("Верно")
        i+=1
    elif i==5 and c2:
        print("Верно")
        i+=1
    elif i==7 and c1:
        print("Верно")
        i+=1
    elif i==9 and c2:
        print("Верно")
        i+=1
else:
    print("Try again")





