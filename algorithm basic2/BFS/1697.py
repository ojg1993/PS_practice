# 1697
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


'''
목표: A와 B의 1차원 좌표상 거리를 이동하는 방법이 걷는방법(X +- 1)과 순간이동하는 방법(2 * X)이 있을때 A와 B가 만나는 가장 빠른 경로를 찾아라.
문제: 최단거리 문제임으로 BFS 알고리즘을 활용하여 걷기와 순간이동을 조합한 최단거리를 찾아야 함
    1. 걷    기: 현재 X좌표에서 한칸씩 이동함 [ 2 -> 3 -> 4 ]
    2. 순간이동: 현재 X좌표의 2배씩 이동함 [ 2 -> 4 -> 8 ]
해결
    1. A와 B의 좌표를 저장
    2. 최대 x좌표 array 저장
    3. X좌표에서 갈 수 있는 목적지를 순차적으로 돌며 이동횟수를 기록
'''

def bfs(start, target):
    q = deque()
    q.append(start)
    
    while q:
        cur = q.popleft()
        if cur == target:
            return axis[cur]
        for n_cur in (cur-1, cur+1, cur*2):
            if 0 <= n_cur <= MAX and not axis[n_cur]:
                axis[n_cur] = axis[cur] + 1
                q.append(n_cur)
        

if __name__ == '__main__':
    A, B = map(int, input().split())
    MAX = 10**5
    axis = [0] * (MAX+1)
    print(bfs(A, B))
