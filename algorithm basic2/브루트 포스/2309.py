# 2309
import sys
from itertools import combinations

input = sys.stdin.readline

dwarves = [int(input()) for _ in range(9)]
for combi in combinations(dwarves, 7):
    if sum(combi) == 100:
        for dwarf in sorted(combi):
            print(dwarf)
        break