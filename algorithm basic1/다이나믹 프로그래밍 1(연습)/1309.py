# 1309


# 규칙성 풀이
n = int(input())
mod = 9901

cache = [[0, 0, 0] for _ in range(n)]
cache[0] = [1, 1, 1]

for i in range(1, n):
    cache[i][0] = (cache[i-1][0] + cache[i-1][1] + cache[i-1][2]) % mod
    cache[i][1] = (cache[i-1][0] + cache[i-1][2]) % mod
    cache[i][2] = (cache[i-1][0] + cache[i-1][1]) % mod


print(sum(cache[n-1]) % mod)


# 점화식 풀이
n = int(input())
mod = 9901

cache = [0] * (n+1)

if n >= 1:
    cache[1] = 3
    if n >= 2:
        cache[2] = 7
        if n >= 3:
            cache[3] = 17
            if n >= 4:
                for i in range(4, n+1):
                    cache[i] = (cache[i-2] + (2 * cache[i-1])) % mod

print(cache[n] % mod)