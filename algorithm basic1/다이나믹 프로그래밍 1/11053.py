# 11053 

n = int(input())
array = list(map(int, input().split()))
cache = [1] * n

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            cache[i] = max(cache[i], cache[j]+1)
            
print(max(cache))