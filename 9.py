arr = [1,2,3,4,5,-6,-7,-8,9,-10]
 
sumPositive = 0
sumNegative = 0
 
for i in range(0, len(arr)):
    if arr[i] > 0:
        sumPositive += arr[i]
    else:
        sumNegative += abs(arr[i])
 
diff = abs(sumNegative - sumPositive)
 
if sumPositive < sumNegative:
    arr.append(diff)
else:
    arr.append(-diff)
 
 
print(f'Сумма отрицательных = {sumNegative}')
print(f'Сумма положительных = {sumPositive}')
print(f'Разница = {diff}')
 
print(arr)