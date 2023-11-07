# 11725
import sys

sys.setrecursionlimit(10 ** 6)
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


'''
    문제: 루트가 없는 무작위 트리가 주어지고 이 트리의 루트를 1이라 할때, 각 노드의 부모 찾기

    조건
        - 2 <= N <= 100,000
        - n-1개의 줄에 부모 노드를 2번 노드부터 오름차순 출력

    세분화 문제
        1. 트리 입력
            -> 인접 행렬 이용
        2. 노드별 부모 구하기
            -> 
        3. 2번 노드부터 순서대로 출력
            -> 
'''

def bfs():
    q = deque()
    q.append(1)

    while q:
        now = q.popleft()
        for next in adj[now]:
            if not ans[next]:
                ans[next] = now
                q.append(next)

if __name__ == '__main__':
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    ans = [0 for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    bfs()

    for i in ans[2:]:
        print(i)