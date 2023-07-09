# 11057

# 1차원
n = int(input())
mod = 10007
cache = [1] * 10

for i in range(n-1):
    for j in range(1, 10):
        cache[j] += cache[j-1]

print(sum(cache) % mod)

# 2차원
n = int(input())
mod = 10007
cache = [[0] * 10 for _ in range(n+1)]
cache[1] = [1] * 10

for i in range(2, n+1):
    for j in range(10):
        cache[i][j] = sum(cache[i-1][j:]) % mod
print(sum(cache[n]) % mod)
