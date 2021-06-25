a=input("Введите строк:")
low=''
up=''
raz=0
gl=0
sgl=0

for i in a:
    if i.islower():
        low=low+i
        if len(low)==2 or (len(low))%2==0:
            raz=raz+1

    elif low!='':
         low=''

for i in a:
    if i in 'a,o,u,y,i,e':
        gl=gl+1
        print(gl)

    else:
        sgl=sgl+1
        print(sgl)

print(raz, len(a),gl, sgl)
