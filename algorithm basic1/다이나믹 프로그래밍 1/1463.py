#1463
n = int(input())
cache = [0] * (n+1)


for i in range(2, n+1):
    cache[i] = cache[i-1] + 1
    if not i % 2:
        cache[i] = min(cache[i], cache[i//2]+1)
    if not i % 3:
        cache[i] = min(cache[i], cache[i//3]+1)


print(cache[n])