a=['apple',52, 623,'rainbow' ,21,1,999,'slash']
w=[]
n=[]
for i in a:
    if type(i) is str:
        w.append(i)
    elif type(i) is int:
        n.append(i)
print(w)
print(n)
w.sort()
n.sort()
a=open('task5.txt','w')
for i in w:
    a.write(i +'\n')
for i in n:
    i = str(i)
    a.write(i +'\n')
a.close()