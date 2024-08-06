# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        ## Iterative
        stk = [(p, q)]

        while stk:
            p, q = stk.pop()

            if p or q:
                if not p or not q or p.val != q.val:
                    return False
                stk.append((p.left, q.left))
                stk.append((p.right, q.right))
        return True
