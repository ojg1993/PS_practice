# 10972
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
nums = sorted((map(int, input().split())))

for c in combinations(nums, m):
    print(c)