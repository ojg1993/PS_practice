# 15664
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted((map(int, input().split())))
ans = set()
for p in combinations(nums, m):
    ans.add(p)

ans = sorted(list(ans))
for _ in ans:
    print(*_)