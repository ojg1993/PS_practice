# 16940
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    visited = [False] * (n + 1)
    q = deque()
    q.append(1)
    visited[1] = True

    idx = 1
    while q:
        cur = q.popleft()
        candidates = []

        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                candidates.append(next)
        if sorted(order[idx:idx+len(candidates)]) == sorted(candidates):
            for i in order[idx:idx+len(candidates)]:
                q.append(i)
            idx += len(candidates)
        else:
            return 0
    return 1

if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    order = list(map(int, input().split()))

    if order[0] == 1:
        print(bfs())
    else:
        print(0)