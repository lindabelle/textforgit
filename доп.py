a=int(input("Введите ваш возраст: "))
if a<18:
    print("Поколение Z")
elif a>18 and a<=35:
    print ("Миллениал")
elif a>=36 and a<=55:
    print ("Поколение X")
elif a>=56 and a<=75:
    print ("Baby-boomer")
elif a>=76 and a<=98:
    print ("Потерянное поколение")
elif a>=99 and a<=120:
    print ("Строители")
else:
    print ("Google it")
