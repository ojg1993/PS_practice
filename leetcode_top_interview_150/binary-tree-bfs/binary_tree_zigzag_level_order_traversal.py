# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root

        from collections import deque

        flag = False
        q = deque([root])
        res = []

        while q:
            snap = len(q)
            level = []

            for _ in range(snap):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if flag:
                res.append(reversed(level))
            else:
                res.append(level)
            flag = True if not flag else False
        return res
