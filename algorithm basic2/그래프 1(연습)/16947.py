# 16947
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def dfs(start, now, cnt, array):
    global cy
    if cnt <= 2:
        for next in stops[now]:
            if not visited[next]:
                visited[next] = True
                dfs(start, next, cnt + 1, array+[next])
                visited[next] = False

    else:
        for next in stops[now]:
            if not visited[next]:
                visited[next] = True
                dfs(start, next, cnt + 1, array+[next])
                visited[next] = False
            else:
                if next == start:
                    cy = True
                    for i in array:
                        cycle.add(i)
                    return

def bfs():
    distance = [-1] * (n+1)
    q = deque()

    for i in range(1, n+1):
        if i in cycle:
            distance[i] = 0
            q.append(i)

    while q:
        now = q.popleft()
        for next in stops[now]:
            if distance[next] == -1:
                q.append(next)
                distance[next] = distance[now] + 1
    print(*distance[1:])


if __name__ == '__main__':
    n = int(input())
    stops = [[] for _ in range(n+1)]
    for _ in range(n):
        a, b = map(int, input().split())
        stops[a].append(b)
        stops[b].append(a)
    visited = [False] * (n + 1)
    cycle = set()
    cy = False

    for i in range(1, n+1):
        if cy:
            break
        visited[i] = True
        dfs(i, i, 1, [i])
        visited[i] = False
    bfs()