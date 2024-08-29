"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def dfs(n, y, x):
            flag = True
            for yy in range(n):
                for xx in range(n):
                    if grid[y][x] != grid[y + yy][x + xx]:
                        flag = False
                        break
            if flag:
                return Node(grid[y][x], True, None, None, None)

            n //= 2
            tl = dfs(n, y, x)
            tr = dfs(n, y, x + n)
            bl = dfs(n, y + n, x)
            br = dfs(n, y + n, x + n)
            return Node(grid[y][x], False, tl, tr, bl, br)

        return dfs(len(grid), 0, 0)
