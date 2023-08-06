# 15655
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
ans = []

for combi in combinations(sorted(nums), m):
    ans.append(combi)

for case in sorted(ans):
    print(*case)