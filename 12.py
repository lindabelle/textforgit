a=int(input())
b=int(input())
c=input("Введите операцию")
if c == "+":
    d=a+b
elif c=="-":
    d=a-b
elif c=="/":
    d=a/b
elif c=="*":
    d=a*b
else:
    print("Некорректная операция")
print(d)
