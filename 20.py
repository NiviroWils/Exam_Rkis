from math import pi 
def fun(a, h, r, m) :
    v1 = a*a*a 
    v2 = r*r*pi*h 
    if v1 <= m and v2 <= m :
        return 'можно заполнить обе емкости'
    elif v1 <= m :
        return 'можно заполнить только куб'
    elif v2 <= m :
        return 'можно заполнить только цилиндр'
    else :
        return 'данным объемом жикости нельзя заполнить обе емкости'
 
a = int(input('введите длину ребра куба: '))
r = int(input('введите радиус цилиндра: '))
h = int(input('введите высоту цилиндра: '))
m = int(input('введите объем жидкости: '))
print(fun(a, h, r, m))