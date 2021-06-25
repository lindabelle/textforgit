a = [4,6,'py','tell',78]
b = [44,'hello',56,'exept',3]
a.extend(b)
print(a)
a.insert(3,500)
print(a)
for i in a:
    if type(i) is str:
        a.remove(i)
print(len(a))









