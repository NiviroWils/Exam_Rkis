sum = 0 # Сумма
countTerms = 0 # Количество слагаемых
 
while True:
    num = int(input())
 
    if num < 0:
        break
 
    if num % 2 != 0:
        sum += -num
    else:
        sum += num * num
 
    countTerms += 1
 
print(f'Сумма = {sum}')
print(f'Количество слагаемых = {countTerms}')