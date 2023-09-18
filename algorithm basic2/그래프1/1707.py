# 1707
import sys
sys.setrecursionlimit(1000000)
def input():
    return sys.stdin.readline().rstrip()

def dfs(s_node, group):
    visited[s_node] = group

    for n_node in graph[s_node]:
        if not visited[n_node]:
            if not dfs(n_node, -group):
                return False
        elif visited[n_node] == visited[s_node]:
            return False
    return True

if __name__ == '__main__':
    k = int(input())
    for _ in range(k):
        v,e = map(int, input().split())
        graph = [[] for _ in range(v)]
        visited = [False] * v

        for _ in range(e):
            a,b = map(lambda x: x-1, map(int, input().split()))
            graph[a].append(b)
            graph[b].append(a)

        for i in range(v):
            if not visited[i]:
                result = dfs(i, 1)
                if not result:
                    break

        print('YES' if result else 'NO')