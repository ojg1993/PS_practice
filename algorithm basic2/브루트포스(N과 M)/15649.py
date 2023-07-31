# 15649
import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

for combi in permutations(range(1,n+1), m):
    print(*combi)
