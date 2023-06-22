# 3003

chess = [1, 1, 2, 2, 2, 8]
now = list(map(int, input().split()))

for i in range(6):
    if chess[i] == now[i]:
        print(0, end=' ')
    else:
        print(chess[i]-now[i], end=' ')