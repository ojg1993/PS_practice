# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # iterative
        stk = [(root, -float("inf"), float("inf"))]

        while stk:
            node, min, max = stk.pop()

            if not (node.val > min and node.val < max):
                return False
            if node.left:
                stk.append((node.left, min, node.val))
            if node.right:
                stk.append((node.right, node.val, max))
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursive
        def valid(node, min, max):
            if not node:
                return True
            if not (node.val > min and node.val < max):
                return False
            return valid(node.left, min, node.val) and valid(node.right, node.val, max)

        return valid(root, -float("inf"), float("inf"))
