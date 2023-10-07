# 16964
import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

def dfs(node):
    if visited[node]: return

    visited[node] = True
    ans_list.append(node)
    for next in graph[node]:
        if not visited[next]:
            dfs(next)

if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    order = list(map(int, input().split()))
    rank = [-1 for i in range(n + 1)]

    # rank -> order 매핑
    for i in range(1, n + 1):
        rank[order[i - 1]] = i
    # 무방향 그래프 -> 트리형 구조변환 및 rank 기준 우선 순위 정렬
    for i in range(1, n + 1):
        graph[i] = sorted(graph[i], key=lambda x: rank[x])

    ans_list = []
    dfs(1)
    print(1 if ans_list == order else 0)