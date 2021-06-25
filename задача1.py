str=input("Введите строку: ")
low=''
upp=''
raz=0
for i in str:
    if i.islower():
        low=low+i
        if len(low)==2:
            raz=raz+1
    elif low != '':
            low = ''

print(raz)
