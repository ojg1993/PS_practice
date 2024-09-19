class Solution:
    def climbStairs(self, n: int) -> int:
        p2, p1 = 1, 2
        if n == 1:
            return p2
        elif n == 2:
            return p1

        for _ in range(3, n+1):
            cur = p1 + p2
            p2, p1 = p1, cur
        return p1
        # dp = [0,1,2] + [0]*(n-2)

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
