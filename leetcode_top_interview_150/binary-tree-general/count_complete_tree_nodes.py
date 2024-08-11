# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        left = self.get_left_depth(root)
        right = self.get_right_depth(root)

        if left == right:
            return (2**left) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_left_depth(self, root):
        depth = 0
        while root:
            root = root.left
            depth += 1
        return depth

    def get_right_depth(self, root):
        depth = 0
        while root:
            root = root.right
            depth += 1
        return depth
