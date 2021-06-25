words=dict()
count=int(input('количество слов в словаре: '))
i=0
while i<count:
    print('vvvod slov')
    wrd=str(input('slovo'))
    value=int(input('Znachenie'))
    if wrd not in words:
        words[wrd]=value
    i=i+1
print(words)
