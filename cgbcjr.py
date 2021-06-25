list=[15,48,'hello',6,19,'world']
l=0
h=0
d=0
for i in list:
    if type(i) is int:
        if i%2==0:
            i=str(i)
            for k in i:
                k=int(i)
                l+=k
            print(i,'summa cifr: ',l)
        else:
            index=list.index(i)
            list[index]=1
    elif type(i) is str:
        for gl in i:
            if gl=='a,o,y,u,i,e':
                h+=1
        else:
            d+=1
    print(i,h)
    print(i,d)
print(list)



