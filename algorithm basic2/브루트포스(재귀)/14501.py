# 14501
import sys
input = sys.stdin.readline


n = int(input())
profits = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if i + profits[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], profits[i][1] + dp[i+profits[i][0]])

print(dp[0])