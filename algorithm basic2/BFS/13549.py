# 13549
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    q = deque()
    q.append(n)

    while q:
        cur = q.popleft()

        if cur == k:
            print(axis[cur])
            exit()

        if 0 <= cur * 2 <= MAX and axis[cur * 2] == -1:
            axis[cur * 2] = axis[cur]
            q.append(cur * 2) # 순간이동 우선순위 고려 첫번째

        if 0 <= cur - 1 <= MAX and axis[cur - 1] == -1:
            axis[cur - 1] = axis[cur] + 1
            q.append(cur - 1)

        if 0 <= cur + 1 <= MAX and axis[cur + 1] == -1:
            axis[cur + 1] = axis[cur] + 1
            q.append(cur + 1)

if __name__ == '__main__':
    n, k = map(int, input().split())
    MAX = 10**5
    axis = [-1] * (MAX+1)
    axis[n] = 0
    bfs()
