a=float(input("Введите число: "))
b=float(input("Введите число: "))
if a%10==0 or b%10==0:
    print("Существует")
    c = float(input("Введите сторону"))
    if a+b>c or b+c>a or a+c>b:
        print("Треугольник существует")
    else:
        print("Не существует")
else:
    if a%2==0 or b%2==0:
        print("correct")
    else:
        b=a**2
        print(b)
