# 14889

import sys
from itertools import combinations

input = sys.stdin.readline


def sol(n, lst):
    global ans
    total_players = range(n)

    for c in combinations(total_players, n // 2):
        start_team = set(c)
        link_team = set(total_players) - start_team

        start_sum = sum(lst[i][j] for i in start_team for j in start_team)
        link_sum = sum(lst[i][j] for i in link_team for j in link_team)

        ans = min(ans, abs(start_sum - link_sum))
    return ans


if __name__ == '__main__':
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    ans = float('inf')

    print(sol(n, array))