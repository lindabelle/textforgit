A=(5,12,88,100,1,96,12,4)
B=(65,88,124,2,0,9,74,55)
sum1=0
sum2=0
for i in A:
    sum1+=i
for i in B:
    sum2+=i
if sum1>sum2:
    print('Сумма А больше')
else:
    print('Сумма B больше')
print(A.index(min(A)))
print(B.index(min(B)))
print(sum(A))