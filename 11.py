import random

N = random.randint(1,10)
arr=[random.randint(-100,100) for i in range(N)]
print(arr)

arrP = []
arrN = []

for i in range(N):
    if arr[i] < 0:
        arrN.append(arr[i])
    if arr[i] > 0:
        arrP.append(arr[i])
    
print(arrN)
print(arrP)