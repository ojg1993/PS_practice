class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten, res = deque(), 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j, 0))

        while rotten:
            for _ in range(len(rotten)):
                y, x, m = rotten.popleft()
                for yy, xx in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                    if 0 <= yy < len(grid) and 0 <= xx < len(grid[0]) and grid[yy][xx] == 1:
                        grid[yy][xx] = 2
                        rotten.append((yy, xx, m+1))
            res = max(res, m)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return res
