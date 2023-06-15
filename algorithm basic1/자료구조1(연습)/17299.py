# 17299

from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
cnt = Counter(array)
stk = []
ans = [-1] * n

for i in range(n):
    while stk and cnt[array[stk[-1]]] < cnt[array[i]]:
        ans[stk.pop()] = array[i]
    stk.append(i)
print(*ans)