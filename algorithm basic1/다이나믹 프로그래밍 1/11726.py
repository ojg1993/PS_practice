# 11726
import sys
sys.setrecursionlimit(10000) # recursion max setting

N = int(input())
mod = 10007

cache = [0] * 1001
cache[1] = 1
cache[2] = 2

# top-down: memoization

def f(n):
    if cache[n]:
        return cache[n]
    else:
        cache[n] = (f(n-1) + f(n-2)) % mod
    return cache[n]

print(f(N))

# bottom-up: tabulation

for i in range(3, 1001):
    cache[i] = (cache[i-1] + cache[i-2]) % mod
    
print(cache[N])
