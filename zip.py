Months={1:'Jan',2:'Fb',3:'March',4:'April',5:'May',6:'Jn',7:'Jl',8:'Ag',9:'St',10:'Oct',11:'Nov',12:'Dec'}
for mn in Months:
    print(mn,': ',Months[mn])

A={'f':10,'a':2,'c':17}
ak=A.keys()
list_ak=list(ak)
list_ak.sort()
B={}
for key in list_ak:
    print('(',key,': ',A[key],')')
    B[key]=A[key]
print(B)
