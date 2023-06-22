# 2563

board = [[0 for i in range(100)] for i in range(100)]

for i in range(int(input())):
    a, b  = map(int, input().split())
    
    for i in range(10):
        for j in range(10):
            if not board[99-b-i][a+j]:
                board[99-b-i][a+j] = 1
            else:
                continue

ans = 0

for i in board:
    ans += sum(i)

print(ans)
