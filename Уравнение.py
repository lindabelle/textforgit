import math
a=int(input("Введите число: "))
b=int(input("Введите число: "))
c=int(input("Введите число: "))
d=b**2-4*a*c
x1=(-b+d**2)/2*a
x2=(-b-d**2)/2*a
x=(-b)/2*a
if d>0:
    print(x1,x2)
elif d==0:
    print ("x")
elif d<0:
    print ("корней нет")

