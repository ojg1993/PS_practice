# 2146
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
d = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

def mark_continents_bfs(y, x, count):
    global visit
    q = deque()
    q.append((y, x))
    continents[y][x] = count
        
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x +dx
            if 0 <= ny < n and 0 <= nx < n and continents[ny][nx] and not visit[ny][nx]:
                visit[ny][nx] = True
                q.append((ny, nx))
                continents[ny][nx] = count

def distance_bfs(count):
    global ans
    q = deque()
    distance = [[-1] * n for _ in range(n)]
    
    # 대륙, 바다 거리 초기화
    for y in range(n):
        for x in range(n):
            if continents[y][x] == count:
                q.append((y,x))
                distance[y][x] = 0    
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            # 범위를 벗어날 때 -> 반복문 통과
            if not 0 <= ny < n or not 0 <= nx < n:
                continue
            # 다른 대륙을 만났을때 -> 최솟값(ans, 현재거리)
            if continents[ny][nx] > 0 and continents[ny][nx] != count:
                ans = min(ans, distance[y][x])
                return
            # 바다를 만났을때 -> 거리 누적합 저장
            if not continents[ny][nx] and distance[ny][nx] == -1:
                distance[ny][nx] = distance[y][x] + 1
                q.append((ny, nx))

    '''
    - 목표: n * n칸의 지도에 대륙간 다리가 놓아지는 가장 짧은 거리 찾기 [2초, 192MB]
    - 문제
        1. 대륙별 차별화 -> BFS 대륙별 마킹
        2. 대륙간 가장 짧은 거리 찾기 -> BFS 타대륙 찾기 
    - 해결
        1. mark_continents_BFS 함수 정의 -> 미방문 좌표중 대륙별 카운트 마킹
        2. distance_BFS 함수 정의 -> 함수호출과 대륙숫자 전달 -> 해당 대륙숫자 <-> 다른 대륙숫자와의 거리 매핑 -> ans 최소값 초기화
    '''
    
if __name__ == '__main__':
    n = int(input())
    continents = [list(map(int, input().split())) for _ in range(n)]
    visit = [[False] * n for _ in range(n)]
    cnt = 1
    ans = float('inf')
    
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and continents[i][j]:
                visit[i][j] = True
                mark_continents_bfs(i, j, cnt)
                cnt += 1
                
    for i in range(1, cnt):
        distance_bfs(i)
    print(ans)