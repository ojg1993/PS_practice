# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        while root:  # move to the left most node
            self.stk.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stk.pop()

        cur = node.right  # if node has right, move to the right and move the left most node
        while cur:
            self.stk.append(cur)
            cur = cur.left
        return node.val

    def hasNext(self) -> bool:
        if self.stk:
            return True
        return False
