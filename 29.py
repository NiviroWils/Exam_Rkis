B = int(input('Введите положительное число B: '))
while B < 0:
    B = int(input('Введите положительное число B: '))  
numbers = int(input('Введите число: '))
summa = 0
while numbers >= 0:
    if numbers % B == 0:
        summa = summa + numbers
    numbers = int(input('Введите число: '))
print('Сумма чисел:', summa)