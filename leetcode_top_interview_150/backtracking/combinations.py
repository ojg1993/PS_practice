class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, arr):
            if len(arr) == k:
                res.append(arr[:])
                return

            for i in range(start, n + 1):
                arr.append(i)
                backtrack(i + 1, arr)
                arr.pop()

        res = []
        backtrack(1, [])
        return res

        # from itertools import combinations
        # return combinations(range(1,n+1), k)
