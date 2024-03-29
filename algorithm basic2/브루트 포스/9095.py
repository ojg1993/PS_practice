# 9095
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [0] * 11
    dp[0], dp[1], dp[2] = 1, 1, 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])