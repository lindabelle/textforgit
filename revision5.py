
for i in range(7):
    if i==0 or i==6:
        for a in range(7):
            print('*',end='')
    else:
        print('*',end='')
        for a in range(1,6):
            print('/', end='')
        print('*',end='')
    print()
