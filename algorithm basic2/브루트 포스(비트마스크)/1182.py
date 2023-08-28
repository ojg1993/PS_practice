# 1182
import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

def sol(lst, target, length):
    global case
    for i in range(1, length+1):
        for combi in combinations(lst, i):
            if sum(combi) == target:
                case += 1

if __name__ == '__main__':
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    case = 0
    sol(arr, S, N)
    print(case)