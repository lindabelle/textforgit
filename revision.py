a=input('Введите строку: ')
c=''
for i in a:
    if not i.isupper():
        c=c+i
        print(c)


