a=input(" print th line")
b=''
for i in a:
    if i.isdigit():
        b=b+i
    elif b!='':
        print(b)
        b = ''
if b!='':
    print(b)
    # смотри фото
