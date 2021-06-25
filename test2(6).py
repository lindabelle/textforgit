a={1:'a',2:'b',3:'c',4:'d'}
try:
    b=a[5]
except KeyError:
    print('нет ключа')
finally:
    print('done')



