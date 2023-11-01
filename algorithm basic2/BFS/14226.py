# 13913
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

'''
문제: 이모티콘 S개를 만들기 위한 최소시간 -> BFS 문제
목표: 복사, 붙여넣기, 1개 삭제로 1 -> S까지 도달하는 최소시간 구하기
해결: 딕셔너리 활용 (현재 갯수, 클립보드의 갯수): 소요시간 -> BFS 구현
    - 현재 이모티콘 복사 및 소요시간 + 1
    - 현재 이모티콘 붙여넣기 및 소요시간 + 1
    - 현재 이모티콘 중 1개 삭제 및 소요시간 + 1
        - 복사: visit= {
            (현재 갯수, 복사 갯수): 이전 소요시간 + 1
        }
        - 붙여넣기: visit= {
            (현재 갯수 + 복사 갯수, 복사갯수): 이전 소요시간 + 1
        }
        - 삭제: visit={
            (현재갯수-1, 복사갯수): 이전 소요시간 + 1
        }
'''

def bfs(start):
    global visit
    q = deque()
    q.append(start)

    while q:
        cur, copied = q.popleft()
        if cur == S:
            return visit[(cur, copied)]
        # 복사
        if (cur, cur) not in visit.keys():
            visit[(cur, cur)] = visit[(cur, copied)] + 1
            q.append((cur, cur))
        # 붙여넣기
        if (cur+copied, copied) not in visit.keys():
            visit[(cur+copied, copied)] = visit[(cur, copied)] + 1
            q.append((cur+copied, copied))
        # 삭제
        if (cur-1 >= 0) and (cur-1, copied) not in visit.keys():
            visit[(cur-1, copied)] = visit[(cur, copied)] + 1
            q.append((cur-1, copied))


if __name__ == '__main__':
    S= int(input())
    visit = dict()
    # 현재 갯수, 클립보드 갯수
    visit[(1, 0)] = 0
    print(bfs((1,0)))
