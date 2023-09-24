# 7562
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
        if y == t_y and x == t_x:
            return chess_board[y][x]
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if (0 <= ny < L) and (0 <= nx < L) and not chess_board[ny][nx]:
                queue.append((ny, nx))
                chess_board[ny][nx] = chess_board[y][x] + 1

if __name__ == '__main__':
    for _ in range(int(input())):
        d = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
        L = int(input())
        s_y, s_x = map(int, input().split())
        t_y, t_x = map(int, input().split())
        chess_board = [[0] * L for _ in range(L)]

        print(bfs(s_y, s_x))