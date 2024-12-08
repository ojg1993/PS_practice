class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2], dp[3] = 1, 2, 5

        for i in range(4, n+1):
            dp[i] = ((dp[i-1] * 2) + dp[i-3]) % (10**9 + 7)
        return dp[-1]
