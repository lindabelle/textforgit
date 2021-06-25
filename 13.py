x = int(input())
if x > 0:
    y = 2 * x - 10
    print(y)
elif x==0:
    y=0
    print(y)
else:
    y = 2 * abs(x) - 10
    print(y)


