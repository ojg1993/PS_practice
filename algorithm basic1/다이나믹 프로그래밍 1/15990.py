# 15990

n = int(input())
mod = 1_000_000_009
lst = [int(input()) for i in range(n)]
cache = [[0] * 4 for _ in range(max(lst)+1)]
cache[1] = [0,1,0,0]
cache[2] = [0,0,1,0]
cache[3] = [0,1,1,1]

for i in range(4, max(lst)+1):
    cache[i][1] = (cache[i-1][2] + cache[i-1][3]) % mod
    cache[i][2] = (cache[i-2][1] + cache[i-2][3]) % mod
    cache[i][3] = (cache[i-3][1] + cache[i-3][2]) % mod

for i in lst:
    print(sum(cache[i]) % mod)