class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        for i in range(1, M):
            grid[i][0] += grid[i-1][0]
        for i in range(1, N):
            grid[0][i] += grid[0][i-1]

        for i in range(1, M):
            for j in range(1, N):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

        # def dfs(y, x, tot):
        #     if y == M-1 and x == N-1:
        #         return
        #     if y < M-1 and tot+grid[y+1][x] < dp[y+1][x]:
        #         dp[y+1][x] = tot+grid[y+1][x]
        #         dfs(y+1, x, tot+grid[y+1][x])
        #     if x < N-1 and tot+grid[y][x+1] < dp[y][x+1]:
        #         dp[y][x+1] = tot+grid[y][x+1]
        #         dfs(y, x+1, tot+grid[y][x+1])

        # M, N = len(grid), len(grid[0])
        # dp = [[float("inf")] * N for _ in range(M)]
        # dp[0][0] = grid[0][0]
        # dfs(0, 0, grid[0][0])
        # return dp[-1][-1]
