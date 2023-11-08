# 1167
import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

'''
    문제: 트리의 노드간 거리가 가장 긴 것 찾기
    조건
        - 2 <= N <= 100,000
        - 가장 거리 출력
        - 간선 정보 [3,1,2,4,3,-1] -> 3과 1의 거리가 2, 3과 4의 거리가 3
            -> -1 은 종료를 의미
    세분화 문제
        1. 노드 간선 정보 및 거리 정보 입력
            -> 2차원 리스트 사용 연결 노드 및 연결 노드까지의 거리 튜플 저장 ex) graph[node] = (adj, dist)
        2. 노드간 거리 합산
            -> BFS활용 트리 지름공식 전개(임의 시작 노드 a에서 가장 먼 b 노드를 구하고 b에서 가장먼 c까지의 거리 구하기)
'''

def bfs(s_node):
    visited = [-1] * (n+1)
    visited[s_node] = 0
    q = deque()
    q.append((s_node, 0))
    res = [0, 0] # 노드, 거리

    while q:
        cur_n, cur_dist = q.popleft()

        for adj_n, dist in graph[cur_n]:
            if visited[adj_n] == -1:
                dist_cal = cur_dist + dist
                q.append((adj_n, dist_cal))
                visited[adj_n] = dist_cal

                if res[1] < dist_cal:
                    res[0], res[1] = adj_n, dist_cal
    return res


if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n+1)]

    for _ in range(n):
        info = list(map(int, input().split()))
        node = info[0]
        idx = 1
        while info[idx] != -1:
            adj_node, distance = info[idx], info[idx+1]
            graph[node].append((adj_node, distance))
            idx += 2

    node, distance = bfs(1)
    print(bfs(node)[1])