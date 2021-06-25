import random
i=1
numb2=0
col2=0
while i <=5:
    numb=random.randint(1,10)
    col=random.randint(1,2)
    numb2=int(input('Введите число от 1 до 10:'))
    col2=int(input('Выберите цвет:'))
    if numb2 ==1 and col2==1:
            print('1 красный')
            numb2 += 1
            col2 += 1
    elif numb2==2 and col2==2:
            print('2 черный')
            numb2 += 1
            col2 += 1
    elif numb2==3 and col2==1:
            print('3 красный')
            numb2 += 1
            col2 += 1
    elif numb2==4 and col2==2:
            print('4 черный')
            numb2 += 1
            col2 += 1
    elif numb2==5 and col2==1:
            print('5 красный')
            numb2 += 1
            col2 += 1
else:

    print("Try one more time")



