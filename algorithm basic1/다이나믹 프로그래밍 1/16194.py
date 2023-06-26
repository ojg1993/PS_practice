# 16194

n = int(input())

# bottom-up
cards = [0] + list(map(int, input().split()))
cache = [float('inf')] * (n+1)
cache[0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        cache[i] = min(cache[i], cache[i-j] + cards[j])
print(cache[n])