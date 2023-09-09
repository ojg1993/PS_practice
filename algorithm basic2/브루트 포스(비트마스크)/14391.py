# 14391
import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    n, m = map(int, input().split())

    paper = [list(map(int, input())) for _ in range(n)]
    ans = []

    for i in range(1 << n * m):
        total = 0
        # 가로합 계산
        for row in range(n):
            r_tot = 0
            for col in range(m):
                # idx는 2차원 행렬을 1줄로 만들었을때의 인덱스
                idx = row * m + col
                if i & (1 << idx) != 0:  # 0이 아니면 가로로 더하기
                    r_tot = r_tot * 10 + paper[row][col]
                else:
                    total += r_tot
                    r_tot = 0
            total += r_tot

        # 세로합 계산
        for col in range(m):
            c_tot = 0
            for row in range(n):
                idx = row * m + col
                if i & (1 << idx) == 0:  # 0일때 세로로 더하기
                    c_tot = c_tot * 10 + paper[row][col]
                else:
                    total += c_tot
                    c_tot = 0
            total += c_tot
        ans.append(total)

    print(max(ans))