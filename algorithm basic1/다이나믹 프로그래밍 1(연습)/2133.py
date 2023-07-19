# 2133

n = int(input())
dp = [1] + [0] * n

if n > 1:
    dp[2] = 3

    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3
        for j in range(0, i - 2, 2):
            dp[i] += dp[j] * 2

print(dp[n])