class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # optimal
        res = 0
        counter = Counter(tuple(row) for row in grid)
        for zipped in zip(*grid):
            res += counter[zipped]  # Counter returns 0 for non existing key
        return res

        # optimal 2
        res = 0
        counter = defaultdict(int)

        for row in grid:
            counter[tuple(row)] += 1
        for col in zip(*grid):
            res += counter[col]
        return res

        # intuition
        r_hm = {i: grid[i] for i in range(len(grid))}
        c_hm = {i: list(zipped) for i, zipped in enumerate(zip(*grid))}
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if r_hm[i] == c_hm[j]:
                    res += 1
        return res
