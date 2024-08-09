# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # recursive
        def preorder(node):
            if not node: return None
            left_tail = preorder(node.left)
            right_tail = preorder(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            return right_tail or left_tail or node
        return preorder(root)

        ## iterative
        # cur = root
        # while cur:
        #     if cur.left:
        #         right_most_from_left = cur.left
        #         while right_most_from_left.right:
        #             right_most_from_left = right_most_from_left.right
        #         right_most_from_left.right = cur.right
        #         cur.right = cur.left
        #         cur.left = None
        #     cur = cur.right



