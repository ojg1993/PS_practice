# 13913
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    q = deque()
    q.append(n)

    while q:
        cur = q.popleft()

        if cur == m:
            print(axis[cur])
            route(cur)

        for next in [cur-1, cur+1, cur*2]:
            if 0 <= next <= MAX and not axis[next]:
                # 이동 횟수: 다음 노드에 전 노드의 경로 거리 + 1
                axis[next] = axis[cur] + 1
                q.append(next)
                # 이동 경로: 다음 노드에 전 노드 저장
                path[next] = cur

def route(start):
    path_order = []

    for _ in range(axis[start]+1):
        path_order.append(start)
        start = path[start]

    print(*path_order[::-1])
    exit()

if __name__ == '__main__':
    n, m = map(int, input().split())
    MAX = 10**5
    # 이동 횟수
    axis = [0] * (MAX+1)
    # 이동 경로
    path = [0] * (MAX+1)
    bfs()
