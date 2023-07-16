# 11054

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

increase = [1] * n
decrease = [1] * n
res = [0] * n

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            increase[i] = max(increase[i], increase[j] + 1)

for i in range(n, -1, -1):
    for j in range(i, n):
        if lst[i] > lst[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

for i in range(n):
    res[i] = increase[i] + decrease[i] -1

print(max(res))