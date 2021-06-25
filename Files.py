f=open("1.txt", "r")
try:
    print(*f)
finally:
    f.close()
with open('1.txt') as f:
    print(*f)
