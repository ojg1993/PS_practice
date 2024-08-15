# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        binary search tree
        1. left values are less than current node
        2. right values are greater than current node
        -> inorder dfs traversal with prev pointer
        """
        # iterative
        prev, res = None, float("inf")
        stk = []
        cur = root

        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left
            node = stk.pop()
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            cur = node.right
        return res

        # recursive
        prev, res = None, float("inf")

        def inorder(cur):
            nonlocal prev, res
            if not cur:
                return

            inorder(cur.left)
            if prev:
                res = min(res, cur.val - prev.val)
            prev = cur
            inorder(cur.right)

        inorder(root)
        return res
