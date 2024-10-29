# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res, max_sum = 0, -float('inf')
        q = deque([(root, 1)])
        
        while q:
            level_sum = 0
            for _ in range(len(q)):
                cur, level = q.popleft()
                level_sum += cur.val

                if cur.left:
                    q.append((cur.left, level+1))
                if cur.right:
                    q.append((cur.right, level+1))
            if level_sum > max_sum:
                max_sum = level_sum
                res = level
        return res