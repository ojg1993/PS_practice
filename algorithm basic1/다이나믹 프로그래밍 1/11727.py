# 11727

import sys
sys.setrecursionlimit(10000)

n = int(input())
mod = 10_007
cache = [0] * 1001
cache[1] = 1
cache[2] = 3
cache[3] = 5
cache[4] = 11

# top-down: memoization
def dp(n):
    if cache[n]:
        return cache[n]
    else:
        cache[n] = dp(n-1) + 2 * dp(n-2)
    return cache[n]
print(dp(n) % mod)

# bottom-up: tabulation
for i in range(5, n+1):
    cache[i] = cache[i-1] + 2 * cache[i-2]

print(cache[n] % mod)