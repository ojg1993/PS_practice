# 1912

n = int(input())
arr = list(map(int, input().split()))

cache = [False] * n
cache[0] = arr[0]

for i in range(1, n):
    cache[i] = max(arr[i], cache[i-1] + arr[i])

print(max(cache))