import random
M=int(input("Введите число: ")) #столбики
N=int(input("Введите число: ")) #строки
A=[[0]*M for i in range(N)]
for i in range(N): # строки
    for j in range(M): #столбики
        A[i][j]=random.randint(1,100)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j],end=' ') # Сначала обращаемся к списку через i[], а затем через j к элементу из i!
    print()
