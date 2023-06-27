# 10844

n = int(input())
mod = 1_000_000_000
cache = [[0] * 10 for _ in range(n+1)]

for i in range(1, 10):
    cache[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j in [0, 9]:
            if not j:
                cache[i][j] = cache[i-1][1]
            else:
                cache[i][j] = cache[i-1][8]
        else:
            cache[i][j] = cache[i-1][j-1] + cache[i-1][j+1]

print(sum(cache[n]) % mod)