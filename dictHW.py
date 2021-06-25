# c={'яблоки':[50,200] ,'персики':[80,220], 'виноград':[92,150]}
# name=input('Введите название товара: ')
# for name in c:
#     if name==c['яблоки']:
#         print(c['яблоки'],'-',[0],'-',[1])
#     elif name==c['персики']:
#         print(c['персики'],'-',[0],'-',[1])
#     elif name==c['виноград']:
#         print(c['виноград'],'-',[0],'-',[1])
#     else:
#         break
# quant=int(input('Введите количество товара: '))
# fin_quant1=(c['яблоки'][0]-quant)
# print('яблоки',fin_quant1)
# fin_quant2=(c['персики'][0]-quant)
# print('персики',fin_quant2)
# fin_quant3=(c['виноград'][0]-quant)
# print('виноград',fin_quant3)
#
goods = {'Apple': [4.5, 10],
         'Orange': [6.2, 5],
         'Pineapple': [10.0, 1],
         'Mango': [7.5, 2],
         'Banana': [3.8, 10]}
for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])
cost=0
while True:
    good=input('What?(n-nothing)')
    if good=='n' or good not in goods.keys():
        break
    qty=int(input('How many?'))
    if qty >goods[good][1]:
        print('We dont have it')
        continue
    cost+=qty*goods[good][0]
    goods[good][1]-=qty
print('price: ', cost)
for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])
