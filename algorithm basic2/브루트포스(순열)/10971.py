# 10971
import sys
input = sys.stdin.readline

def dfs(start, now, tot, cnt):
    global ans
    if cnt == n:
        if costs[now][start]:
            tot += costs[now][start]
            if tot < ans:
                ans = tot
        return

    if tot > ans:
        return

    for i in range(n):
        if not v[i] and costs[now][i]:
            v[i] = True
            dfs(start, i, tot+costs[now][i], cnt+1)
            v[i] = False

if __name__ == '__main__':
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    v = [False] * n
    ans = float('inf')

    for i in range(n):
        v[i] = True
        dfs(i,i,0,1)
        v[i] = False
    print(ans)