print('''Вводите текст, отделяя строки
нажатием Enter, последней строкой
введите слово Конец''')
while True:
    s = str(input())
    if(s=='Конец' or s=='конец'):
        break
    k = 0
    for x in s:
        if x in 'ёуеыаоэяиюЁУЕЫАОЭЯИЮ':
            k += 1
    print(k)