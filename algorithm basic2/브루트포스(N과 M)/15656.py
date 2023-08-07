# 15656
import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for p in product(sorted(nums), repeat=m):
    print(*p)
