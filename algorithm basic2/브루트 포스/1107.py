# 1107
import sys

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input())
btn = list(input().split())

ans = abs(100 - n)

if not ans:
    print(0)
else:
    for i in range(1_000_001):
        for j in str(i):
            if j in btn:
                break
        else:
            ans = min(ans, len(str(i)) + abs(i - n))
    print(ans)