# 15654
import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
ans = []

for p in permutations(nums, m):
    ans.append(p)

for case in sorted(ans):
    print(*case)