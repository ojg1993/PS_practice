# 14889
import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

def sol(team_cnt, arr):
    global tot, ans

    for combi in combinations(arr, team_cnt//2):
        ans = min(ans, abs(tot - sum(combi)))
        if not ans:
            break
    return ans

if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    r_sum = [sum(i) for i in arr]
    c_sum = [sum(i) for i in zip(*arr)]

    n_arr = [i + j for i, j in zip(r_sum, c_sum)]
    tot = sum(n_arr) // 2
    ans = float('inf')

    print(sol(n, n_arr))