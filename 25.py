import random

N = random.randint(1,15)
arr = [random.randint(-100,100) for i in range(N)]
print(arr)
K = 0
T = 0
t = 0
for i in range(N):
    if arr[i] % 3 == 0:
        K += 1
print("Number of multiples of three: " + str(K))

for i in range(N):
    if arr[i] % 2 == 0:
        T += arr[i]
        t += 1

A = T/t
print("Arithmetic mean: " + str(A))

arr.insert(0 , K)
arr.append(A)
print(arr)