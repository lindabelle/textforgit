try:
    a=int(input('Print first number: '))
    b=int(input('Print second number: '))
    c=a/b
except ZeroDivisionError:
    print("Mistake")
else:
    d=c**2
    print(d)
finally:
    print("Done")
