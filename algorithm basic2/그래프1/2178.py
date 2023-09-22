# 2178
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if (0 <= ny < n) and (0 <= nx < m) and maze[ny][nx] == 1:
                queue.append((ny, nx))
                maze[ny][nx] = maze[y][x] + 1

    return maze[n-1][m-1]

if __name__ == '__main__':
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m = map(int, input().split())

    maze = [list(map(int, input())) for _ in range(n)]
    print(bfs(0,0))