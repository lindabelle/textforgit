body={'левая рука','правая рука','левая нога','правая нога'}
color={'красный','синий','зеленый','желтый'}
step={'1','2','3','4','5','6','7','8'}
option=input('Введите цвет: ')
option2=int(input("Введите номер хода: "))
for i in color:
    while color=='красный' or 'синий':
        i+=1
        print(body,color,step)
    else:
        print("Try again")
    while step<5:
        step+=1
    else:
        break




