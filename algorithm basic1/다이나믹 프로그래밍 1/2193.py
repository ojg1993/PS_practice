# 2193

n = int(input())

cache = [0] * (n+1)
cache[1] = 1

# bottom up
for i in range(2, n+1):
    cache[i] = cache[i-1] + cache[i-2]

print(cache[n])