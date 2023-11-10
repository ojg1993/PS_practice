# 1967
import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

'''
    문제: 트리의 노드간 가중치가 가장 큰 경로 찾기
    조건
        - 2 <= N <= 100,000
        - 가중치가 가장 큰 경로 출력
        - 간선 정보 [3,1,2] -> 3과 1의 거리가 2
    세분화 문제
        1. 노드 간선 정보 및 거리 정보 입력
            -> 2차원 리스트 사용 연결 노드 및 연결 노드까지의 거리 튜플 저장 ex) graph[node].appned((adj, dist))
        2. 노드간 거리 합산
            -> BFS활용 트리 지름공식 전개(임의 시작 노드 a에서 가중치가 가장 큰 b 노드를 구하고,
               b에서부터 가중치가 가장 큰 c까지의 가중치 구하기)
'''

def bfs(s_node):
    visited = [-1] * (n+1)
    visited[s_node] = 0
    q = deque()
    q.append((s_node, 0))
    res = [0,0]
    
    while q:
        cur_node, cur_weight = q.popleft()
        
        for next_node, next_weight in graph[cur_node]:
            if visited[next_node] == -1:
                new_weight = cur_weight + next_weight
                q.append((next_node, new_weight))
                visited[next_node] = new_weight
                
                if res[1] < new_weight:
                    res = [next_node, new_weight]
    return res
        


if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n+1)]
   
    for _ in range(n-1):
       a, b, w = map(int, input().split())
       graph[a].append((b, w))
       graph[b].append((a, w))
   
    node, weight = bfs(1)
    print(bfs(node)[1])