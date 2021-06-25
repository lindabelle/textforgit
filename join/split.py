s=input("Введите строку")
a=s.split()
b=' '.join(a)
print(b)
if s==b[::-1]:
    print("correct")
else:
    print("wrong")

