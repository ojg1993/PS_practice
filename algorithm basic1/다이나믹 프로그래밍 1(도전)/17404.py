# # 17404
import sys

input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
res = float('inf')

for i in range(3):
    dp = [[float('inf')] * 3 for _ in range(n)]
    dp[0][i] = cost[0][i]

    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + cost[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + cost[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + cost[j][2]

    dp[-1][i] = float('inf')
    res = min(res, min(dp[-1]))
print(res)