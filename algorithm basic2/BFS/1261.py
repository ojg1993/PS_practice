# 1261
import sys

sys.setrecursionlimit(10 ** 6)
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def bfs():
    q = deque()
    q.append((0, 0))
    wall_cnt = [[-1] * (n + 1) for _ in range(m + 1)]
    wall_cnt[0][0] = 0  # 초기값 방문처리

    while q:
        y, x = q.popleft()

        if (y, x) == (m - 1, n - 1):
            return wall_cnt[m - 1][n - 1]

        for dy, dx in step:
            ny, nx = y + dy, x + dx

            if (0 <= ny < m) and (0 <= nx < n) and wall_cnt[ny][nx] == -1:  # 범위 내 & 미방문

                if not maze[ny][nx]:  # 빈방이면
                    wall_cnt[ny][nx] = wall_cnt[y][x]  # 벽 누적값 전달
                    q.appendleft((ny, nx))  # 빈방 순회 우선

                else:  # 벽이면
                    wall_cnt[ny][nx] = wall_cnt[y][x] + 1  # 벽 누적값 + 1
                    q.append((ny, nx))


if __name__ == '__main__':
    n, m = map(int, input().split())  # n: x , m = y
    maze = [list(map(int, input())) for _ in range(m + 1)]
    step = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    print(bfs())

# Key Point: 벽을 깬 횟수가 가장 작아야 하므로,
#            이동할 수 있는 가장 먼 빈 방으로 '우선' 이동할 수 있도록 Queue 사용
