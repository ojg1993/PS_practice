# 10974
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
target = [k for k in range(1, n+1)]
for p in permutations(target, n):
    print(*p)