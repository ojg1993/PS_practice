class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(y, x):
            grid[y][x] = "0"
            for yy, xx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if 0 <= yy < M and 0 <= xx < N and grid[yy][xx] == "1":
                    dfs(yy, xx)

        M, N = len(grid), len(grid[0])
        res = 0
        for y in range(M):
            for x in range(N):
                if grid[y][x] == "1":
                    dfs(y, x)
                    res += 1
        return res
