# 2667
from collections import deque
import sys
sys.setrecursionlimit(1000000)
def input():
    return sys.stdin.readline().rstrip()

def count_houses(complex, y, x):
    queue = deque()
    queue.append((y, x))
    complex[y][x] = 0
    house_cnt = 1

    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            ny = y + dy
            nx = x + dx

            if (0 <= ny < n) and (0 <= nx < n) and complex[ny][nx]:
                complex[ny][nx] = 0
                queue.append((ny, nx))
                house_cnt += 1
    return house_cnt

if __name__ == '__main__':
    d = [(1, 0), (-1, 0), (0, 1),(0, -1)]

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