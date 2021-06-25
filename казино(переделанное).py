import random
i=1
numb2=0
col2=0
while i <=5:
    numb=random.randint(1,10)
    col=random.randint(1,2) # 1 красные,2 черные
    numb2=int(input('Введите число от 1 до 10:'))
    col2=int(input('Выберите цвет:'))
    if numb2%2==numb and col2==col:
        print(numb2, 'красные')
        i+=1
    else:
        print(numb2, 'черные')
        i+=1



