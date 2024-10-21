# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # if not root: return 0

        # stk = [(root, 1)]
        # res = 1
        # while stk:
        #     node, level = stk.pop()
        #     res = max(res, level)
        #     if node.right:
        #         stk.append((node.right, level+1))
        #     if node.left:
        #         stk.append((node.left, level+1))
        # return res
