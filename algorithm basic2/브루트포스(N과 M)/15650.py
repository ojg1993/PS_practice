# 15650
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

for combi in combinations(range(1,n+1), m):
    print(*combi)