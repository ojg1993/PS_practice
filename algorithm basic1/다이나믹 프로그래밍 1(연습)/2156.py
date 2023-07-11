# 2156

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
wine = [0] + [int(input()) for _ in range(n)]
dp[1] = wine[1]

if n > 1:
    dp[2] = wine[1] + wine[2]
    if n > 2:
        for i in range(3, n+1):
            dp[i] = max(dp[i-1],
                        wine[i] + dp[i-2],
                        wine[i] + wine[i-1] + dp[i-3]
                        )

print(max(dp))

# [0, a, b, c, ... x] 까지의 와인이 있다고 칠때
# c를 마시지 않는 경우: dp[i-1] -> c 빼고 누적
# b를 마시지 않는 경우: dp[i-2] + wine[i] -> b 빼고 누적
# a를 마시지 않는 경우: dp[i-3] + wine[i-1] + wine[i] -> a 빼고 누적