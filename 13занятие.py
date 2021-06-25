a=['кот','слон','змея']
 b=a.copy()
 print(a,b)
 d=list(a)
 print(a,d)
import copy
# e=copy.copy(a)
# print(a,e)
f=copy.deepcopy(a)#для всех вложенных
print(a,f)
c=a[:]
print(a,c)

