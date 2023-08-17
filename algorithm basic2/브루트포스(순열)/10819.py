# 10819
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
target = list(map(int, input().split()))
ans = 0

for p in permutations(target, n):
    tmp = 0
    for i in range(n-1):
        tmp += abs(p[i] - p[i+1])
    ans = max(ans, tmp)

print(ans)