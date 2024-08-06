# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ### 1. DFS recursive O(n), O(n)
        def traverse(cur, level):
            if not cur:
                return level
            left = traverse(cur.left, level + 1)
            right = traverse(cur.right, level + 1)
            return max(left, right)

        return traverse(root, 0)

        ### 2. DFS recursive O(n), O(n)
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        ### 3. DFS iterative O(n), O(n)
        stk = [(root, 1)]
        res = 0

        while stk:
            cur, depth = stk.pop()
            if cur:
                res = max(res, depth)
                stk.append((cur.right, depth + 1))
                stk.append((cur.left, depth + 1))
        return res

        ### 4. BFS iterative O(n), O(n)
        from collections import deque

        if not root:
            return 0

        q = deque([root])
        depth = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1
        return depth
