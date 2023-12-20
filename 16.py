a = int(input())   #edge
h = int(input())   #height
r = int(input())   #radius
m = int(input())   #volume
v1 = a * a * a  #cube volume
v2 = 3.14159 * r**2 * h   #cilinder volume
if m > v1 and m > v2:
    print('Не поместится в обе емкости')
if m > v1:
    print('Не поместится в первую емкость')
if m > v2:
    print('Не поместится во вторую емкость')
if m <= v1 and m <= v2:
    print('Поместится в обе емкости')
if m <= v1:
    print('Поместится в первую емкость')
if m <= v2:
    print('Поместится во вторую емкость')