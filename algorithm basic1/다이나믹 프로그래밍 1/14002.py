# 14002

n = int(input())
array = list(map(int, input().split()))
cache = [1] * n

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            cache[i] = max(cache[i], cache[j]+1)
ans = max(cache)
print(ans)

arr = []

for i in range(n-1, -1, -1):
    if cache[i] == ans:
        arr.append(array[i])
        ans -= 1
print(*reversed(arr))