# 17298

import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
stk = []
ans = [-1] * n

for i in range(n):
    while stk and array[stk[-1]] < array[i]:
        ans[stk.pop()] = array[i]
    stk.append(i)
print(*ans)