numbers = int(input('Введите число: '))
positive = 0
negative = 0
while numbers != -65432:
    if numbers >= 0:
        positive += 1
    else:
        negative += 1
    numbers = int(input('Введите число: '))    
_sum = negative + positive
print('Процент положительных чисел: ', round(positive / _sum, 2) * 100, '%',
      '\nПроцент отрицательных чисел: ', round(negative / _sum, 2) * 100, '%')