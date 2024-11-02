# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left:
                root.val = self.get_next_val(root, 0)
                root.left = self.deleteNode(root.left, root.val)
            elif root.right:
                root.val = self.get_next_val(root, 1)
                root.right = self.deleteNode(root.right, root.val)
        return root

    def get_next_val(self, node, direction):
        if direction:
            node = node.right
            while node and node.left:
                node = node.left
        else:
            node = node.left
            while node and node.right:
                node = node.right
        return node.val
