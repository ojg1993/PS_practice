# 10810

n, m = map(int, input().split())
basket = [ 0 for i in range(n)]

for i in range(m):
    i, j, k = map(int, input().split())
    for h in range(i, j+1):
        basket[h - 1] = k

print(*basket)