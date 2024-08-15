# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive
        self.k = k
        self.res = None

        def inorder(node):
            if not node or self.res:
                return
            inorder(node.left)
            self.k -= 1
            if not self.k:
                self.res = node.val
                return
            inorder(node.right)

        inorder(root)

        return self.res

        # iterative
        stk = []

        while stk or root:
            while root:
                stk.append(root)
                root = root.left

            node = stk.pop()

            k -= 1
            if not k:
                return node.val

            root = node.right
