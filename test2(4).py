cake={'napoleon':['flour,sugar,artificial stuff',999,10]}
name=input('Введите название продукта: ,n-ничего')
if name=='n' or name not in cake.keys():
    break
elif: discr=input('Наберите discr чтобы увидеть описание: ')
        print(cake.keys())
elif:
    price=input('Наберите price чтобы увидеть описание: ')
        print(cake['napoleon'][1])
elif:
    qnt=input('Наберите qnt чтобы увидеть количество: ')
        print(cake[2])
        if qnt > cake['napoleon'][2]:
            print('We dont have it')
    else:
        for key, value in cake.items():
            print(key, '-', value[0], '-', value[1])





