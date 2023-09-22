# 4963
from collections import deque
import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    islands[y][x] = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if (0 <= ny < h) and (0 <= nx < w) and islands[ny][nx]:
                islands[ny][nx] = 0
                queue.append((ny, nx))

if __name__ == '__main__':
    d = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    while True:
        w, h = map(int, input().split())
        if not w and not h:
            break
        islands = [list(map(int, input().split())) for _ in range(h)]
        cnt = 0

        for i in range(h):
            for j in range(w):
                if islands[i][j]:
                    bfs(i, j)
                    cnt += 1
        print(cnt)
