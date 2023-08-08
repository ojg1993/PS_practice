# 15663
import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted((map(int, input().split())))
ans = set()
for p in permutations(nums, m):
    ans.add(p)

ans = sorted(list(ans))
for _ in ans:
    print(*_)