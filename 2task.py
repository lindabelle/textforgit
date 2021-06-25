a=input("Введите текст: ")
gl=0
sgl=0
e=''
for i in a:
    if i in 'a,o,u,y,i,e':
        gl=gl+1

    else:
        sgl=sgl+1
        e=e+i
if gl>sgl:
    a=(gl/sgl*100)-100
    print(a)
else:
    print(e)