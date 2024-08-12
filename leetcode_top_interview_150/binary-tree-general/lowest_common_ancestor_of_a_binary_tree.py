# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        """
        looking for node that has p and q as decendants
        1. p and q can be on one side such that left or right
          -> move cur node to the side
        2. p and q can be on both side such that p on left and q on right
          - > cur node is the answer
        """

        def dfs(node):
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)
            cur = node == p or node == q

            if (left and right) or (cur and left) or (cur and right):
                self.res = node
                return
            return left or right or cur

        dfs(root)
        return self.res
