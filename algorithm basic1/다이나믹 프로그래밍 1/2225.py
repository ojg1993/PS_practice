# 2225

n, k = map(int, input().split())

cache = [ [0] * (k+1) for _ in range(n+1) ]
cache[0][0] = 1

for i in range(n+1):
    for j in range(1, k+1):
        cache[i][j] = cache[i-1][j] + cache[i][j-1]

print(cache[n][k] % 1_000_000_000)
