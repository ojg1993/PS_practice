# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        from collections import deque

        res = []
        q = deque([root])

        while q:
            snap = len(q)
            level_sum = 0
            for _ in range(snap):
                cur = q.popleft()  # FIFO
                level_sum += cur.val
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
            res.append(level_sum / snap)
        return res
