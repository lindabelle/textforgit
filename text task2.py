f = open('task2.txt')
s = f.readlines()
print(s)
n=[]
w=[]
for i in s:
    i=i[:-1]
    print(i)
    if i.isdigit():
        i=int(i)
        n.append(i)
    elif  i.isalpha():
        i=str(i)
        w.append(i)
print(n)
print(w)
n.sort()
w.sort()
m=n+w
print(m)

