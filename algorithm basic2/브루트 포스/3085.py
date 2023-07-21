# 3085
import sys

input = sys.stdin.readline


def bomboni(data):
    max_cnt = 1
    for i in range(n):

        cnt = 1
        for j in range(1, n):
            if data[i][j] == data[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

        cnt = 1
        for j in range(1, n):
            if data[j][i] == data[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt


n = int(input())
lst = [list(input().rstrip()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
            cnt = bomboni(lst)
            ans = max(ans, cnt)
            lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]

        if i + 1 < n:
            lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]
            cnt = bomboni(lst)
            ans = max(ans, cnt)
            lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]
print(ans)