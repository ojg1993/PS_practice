# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n), O(n)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, prev):
            if not node:
                return

            cur = prev + node.val
            self.res += self.h[cur-targetSum]

            self.h[cur] += 1
            dfs(node.left, cur)
            dfs(node.right, cur)
            self.h[cur] -= 1

        self.res = 0
        self.h = defaultdict(int)
        self.h[0] = 1  # a single node meeting the criteria
        dfs(root, 0)
        return self.res

    # O(2^n), O(n)
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    #     def helper(node, val):
    #         if not node: return
    #         if val == targetSum:
    #             self.cnt += 1

    #         if node.left:
    #             helper(node.left, val + node.left.val)
    #         if node.right:
    #             helper(node.right, val + node.right.val)

    #     def dfs(node):
    #         if not node: return

    #         helper(node, node.val)
    #         if node.left:
    #             dfs(node.left)
    #         if node.right:
    #             dfs(node.right)

    #     self.cnt = 0
    #     dfs(root)
    #     return self.cnt
