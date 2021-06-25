a={1:'j',2:'h',3:'g',55:'gt',12:'jk',8:'jhh'}
b=a.keys()
c=list(b)
c.sort()
print(c)
B={}
for i in c:
    print('(', i,":",a[i],')')
B[i]=a[i]
print(B)









