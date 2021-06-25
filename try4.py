while True:
    a=input('Введите предложение')
    b=input('Введите предложение')
    try:
        result=int(a)/int(b)
    except valueError:
        print("Only numbers allowed")
    except ZeroDivisionError:
        print("No zero division")
    else:
        print('Result')