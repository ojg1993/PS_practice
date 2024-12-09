class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [
            [1 if not r or not c else 0 for c in range(n)] for r in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[-1][-1]
