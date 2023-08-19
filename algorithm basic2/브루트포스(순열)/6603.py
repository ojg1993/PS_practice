# 6603
import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    candidates = list(map(int, input().split()))

    if candidates[0] == 0:
        break
    else:
        candidates = sorted(candidates[1:])
        for combi in combinations(candidates, 6):
            print(*combi)
        print()