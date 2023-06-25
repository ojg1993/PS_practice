# 11052

n = int(input())
cost = [0] + list(map(int, input().split()))
cache = [0] * (n+1)

# bottom up
for i in range(1, n+1):
    for j in range(1, i+1):
        cache[i] = max(cache[i], cache[i-j] + cost[j])
print(cache[n])