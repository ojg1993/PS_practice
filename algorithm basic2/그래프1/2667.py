# 2667
from collections import deque
import sys
sys.setrecursionlimit(1000000)
def input():
    return sys.stdin.readline().rstrip()

def count_houses(graph, y, x):
    queue = deque()
    queue.append((y, x))
    graph[y][x] = 0
    house_cnt = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if graph[ny][nx]:
                graph[ny][nx] = 0
                queue.append((ny, nx))
                house_cnt += 1
    return house_cnt

if __name__ == '__main__':
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    n = int(input())
    complexes = [list(map(int, input())) for _ in range(n)]
    complex_cnt = []

    for i in range(n):
        for j in range(n):
            if complexes[i][j]:
                complex_cnt.append(count_houses(complexes, i, j))

    complex_cnt.sort()
    print(len(complex_cnt))
    for i in range(len(complex_cnt)):
        print(complex_cnt[i])