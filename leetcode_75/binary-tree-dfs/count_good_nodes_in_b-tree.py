# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, x):
            nonlocal res
            if not node: return
            if node.val >= x:
                x = node.val
                res += 1
            dfs(node.left, x)
            dfs(node.right, x)
            
        res = 0
        dfs(root, root.val)
        return res