class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(num, arr):
            if sum(arr) > n or len(arr) > k:
                return
            if sum(arr) == n and len(arr) == k:
                res.append(arr.copy())

            for nxt in range(num + 1, 10):
                arr.append(nxt)
                if not backtrack(nxt, arr):
                    return arr.pop()
                arr.pop()

        res = []
        backtrack(0, [])
        return res
