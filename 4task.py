a=int(input("Введите первое число промежутка: "))
b=int(input("Введите второе число промежутка: "))
c=int(input("Введите количество делителей: "))
while a<=b:
    i=45
    for i in range(45,b):
        if a%i==0:
            i+=1
            for i in range(1,a+1):
                if a%i==0:
                    print (i)
    a+=1
