import random

N = random.randint(1,10)
arr=[random.randint(0,1) for i in range(N)]
print(arr)

for i in range(N):
    if arr[i] == 0:
        arr[i] = []


print(arr)