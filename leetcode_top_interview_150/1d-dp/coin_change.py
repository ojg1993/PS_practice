class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        coins.sort()

        for a in range(1, amount + 1):
            for c in coins:
                diff = a - c
                if diff < 0:
                    break
                dp[a] = min(dp[a], 1 + dp[diff])
        return dp[-1] if dp[-1] != amount + 1 else -1
