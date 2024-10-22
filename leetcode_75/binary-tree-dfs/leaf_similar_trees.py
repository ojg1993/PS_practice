# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node, leaves):
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.left:
                get_leaves(node.left, leaves)
            if node.right:
                get_leaves(node.right, leaves)

            return leaves
        
        return get_leaves(root1, []) == get_leaves(root2, [])