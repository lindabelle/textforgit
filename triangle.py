a=int(input("Введите первую сторону: "))
b=int(input("Введите вторую сторону: "))
c=int(input("Введите третью сторону: "))
if a+b<=c or a+c<=b or b+c<=a:
    print("Это не треугольник")
elif a!=b and b!=c and c!=a:
    print("Треугольник разносторонний")
elif a==b==c:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")


