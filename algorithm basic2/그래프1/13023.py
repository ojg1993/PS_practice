# 13023
import sys
def input():
    return sys.stdin.readline().rstrip()

def dfs(idx, number):
    if number == 4:
        print(1)
        exit()
    for i in adjacent[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False


if __name__ == '__main__':
    n, m = map(int, input().split())
    adjacent = [[] for _ in range(n)]
    visited = [False] * n
    ans = False

    for _ in range(m):
        a, b = map(int, input().split())
        adjacent[a].append(b)
        adjacent[b].append(a)

    for i in range(n):
        visited[i] = True
        dfs(i, 0)
        visited[i] = False
    print(0)