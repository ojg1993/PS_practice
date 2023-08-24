# 15661

import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def sol(n, lst):
    global ans, tot

    for i in range(1, n // 2 + 1):
        for combi in combinations(lst, i):
            ans = min(ans, abs(tot - sum(combi)))
            if not ans:
                break
        if not ans:
            break
    return ans



if __name__ == '__main__':
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    row = [sum(i) for i in array]
    col = [sum(i) for i in zip(*array)]

    n_array = [i + j for i, j in zip(row, col)]
    tot = sum(n_array) // 2
    ans = float('inf')

    print(sol(n, n_array))