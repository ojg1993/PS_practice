# 1260
import sys
def input():
    return sys.stdin.readline().rstrip()

def dfs(s_node):
    visited[s_node] = True
    print(s_node, end=' ')

    for n_node in range(1, n+1):
        if not visited[n_node] and graph[s_node][n_node]:
            dfs(n_node)

def bfs():
    while queue:
        cur = queue.pop(0)
        print(cur, end=' ')
        for n_node in range(1, n+1):
            if not visited[n_node] and graph[cur][n_node]:
                visited[n_node] = True
                queue.append(n_node)


if __name__ == '__main__':
    n, m, v = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):
        a,b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1

    dfs(v)
    print()

    visited = [False] * (n+1)
    visited[v] = True
    queue = [v]
    bfs()
