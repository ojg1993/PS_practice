# 7576
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if (0 <= ny < n) and (0 <= nx < m) and not tomatoes[ny][nx]:
                queue.append((ny, nx))
                tomatoes[ny][nx] = tomatoes[y][x] + 1

if __name__ == '__main__':
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    m, n = map(int, input().split())
    tomatoes = [list(map(int, input().split())) for _ in range(n)]
    queue = deque()
    ans = 0

    for i in range(n):
        for j in range(m):
            if tomatoes[i][j] == 1:
                queue.append((i,j))
    bfs()

    for line in tomatoes:
        for tomato in line:
            if not tomato:
                print(-1)
                exit()
        ans = max(max(line), ans)
    print(ans-1)