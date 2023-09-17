# 11724
import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

def dfs(s_node):

    for n_node in range(1, n+1):
        if not visited[n_node] and graph[s_node][n_node]:
            visited[n_node] = True
            dfs(n_node)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1
    
    visited = [False] * (n+1)
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            cnt += 1
            visited[i] = True
            dfs(i)

print(cnt)