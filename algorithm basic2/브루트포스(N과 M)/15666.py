# 15666
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted((map(int, input().split())))
ans = set()
for c in combinations_with_replacement(nums, m):
    ans.add(c)

ans = sorted(list(ans))
for _ in ans:
    print(*_)