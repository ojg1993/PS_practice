# 13023
import sys
def input():
    return sys.stdin.readline().rstrip()

def dfs(idx, depth):
    if depth == 5:
        print(1)
        exit()
    else:
        for g in graph[idx]:
            if not visited[g]:
                visited[g] = True
                dfs(g, depth+1)
                visited[g] = False

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    visited = [False] * n

    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(n):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False
    print(0)