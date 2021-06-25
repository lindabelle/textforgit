s=input()
upp=''
low=''
for i in s:
    if i.islower():
        low=low+i
    elif i.isupper():
        upp=''
print(low)


