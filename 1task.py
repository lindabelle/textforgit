number=int(input("Введите число:"))
chet=0
nechet=0
for i in str(number):
    i=int(i)
    if i%2==0:
        chet=chet+1

    else:
        nechet=nechet+1
print('cht')
print('ncht')
sum=0
proiz=1
if chet>nechet:
    for i in str(number):
        i=int(i)
        sum=sum+i
else:
    number=str(number)
    proiz=int(number[0])* int(number[2])*int(number[5])

print(sum)
print(proiz)