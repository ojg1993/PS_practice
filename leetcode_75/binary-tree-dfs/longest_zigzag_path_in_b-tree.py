# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zigzag(cur, left, right):
            if not cur:
                return

            self.res = max(self.res, left, right)
            zigzag(cur.left, right+1, 0)
            zigzag(cur.right, 0, left+1)

        self.res = 0
        zigzag(root, 0, 0)
        return self.res return self.res
