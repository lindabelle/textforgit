massiv=[2,5,1,8,3,6,9]
count=0
uncount=0
for i in massiv:
    if i%2==0:
        count+=1
    elif i%2!=0:
        uncount+=1
print(count,"Chet", uncount,"Necheet")
sum=0
pr=1
if count>uncount:
        for i in massiv:
            sum=sum+i
            print(sum)
else:
    pr=massiv[0]*massiv[2]*massiv[5]
    print(pr)











