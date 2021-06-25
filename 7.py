from math import pi
r=float(input("Введите радиус: "))
h=float(input("Введите высоту"))

s= 2*(pi*r**2)
c = 2*pi*r*h
d = s+c
print(round(d,2))

