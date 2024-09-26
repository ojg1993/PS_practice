class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        grid       dp 
        0 0 0     0 0 0
        0 x 0  -> 0 0 0
        0 0 0     0 0 1
        """
        def dfs(y, x):
            if y == M or x == N or obstacleGrid[y][x]:
                return 0
            if (y, x) in cache:
                return cache[(y, x)]
            cache[(y, x)] = dfs(y+1, x) + dfs(y, x+1)
            return cache[(y, x)]

        M, N = len(obstacleGrid), len(obstacleGrid[0])
        cache = {(M-1, N-1): 1}
        return dfs(0, 0)

        # DP
        # M, N = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [0] * N
        # dp[-1] = 1

        # for i in reversed(range(M)):
        #     for j in reversed(range(N)):
        #         if obstacleGrid[i][j]:
        #             dp[j] = 0
        #         elif j < N-1:
        #             dp[j] = dp[j] + dp[j+1]
        # return dp[0]
