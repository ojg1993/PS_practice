# 9095

cache = [0] * 11
cache[1] = 1
cache[2] = 2
cache[3] = 4
cache[4] = 7
cache[5] = 13

# top-down
def dp(n):
    if cache[n]:
        return cache[n]
    else:
        cache[n] = dp(n-1) + dp(n-2) + dp(n-3)
    return cache[n]

for i in range(int(input())):
    n = int(input())
    print(dp(n))
    
# bottom-up
    for i in range(6, n+1):
        cache[i] = cache[i-1] + cache[i-2] + cache[i-3]
    print(cache[n])
