M = 3
arr = []
 
for i in range(M):
    arr.append(input())
 
arr.sort()
arr.reverse()
 
print(f'Саммая длинная строка - {arr[0]} = {len(arr[0])} символов')
 
for i in range(len(arr)):
    print('*' * len(arr[i]) + arr[i])