# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # dfs iterative
        # if not root: return False
        # stk = [(root, root.val)]

        # while stk:
        #     cur, val = stk.pop()

        #     if not cur: continue
        #     if not cur.left and not cur.right and val == targetSum:
        #         return True
        #     stk.append((cur.right, val+cur.val))
        #     stk.append((cur.left, val+cur.val))

        # return False

        # dfs recursive
        def dfs(node, tot):
            if not node:
                return False

            tot += node.val
            if not node.left and not node.right and tot == targetSum:
                return True
            return dfs(node.left, tot) or dfs(node.right, tot)

        return dfs(root, 0)
