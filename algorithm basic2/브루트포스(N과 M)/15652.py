# 15652
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())

for combi in combinations_with_replacement(range(1,n+1), m):
    print(*sorted(combi))