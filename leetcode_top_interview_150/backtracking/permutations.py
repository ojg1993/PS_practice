class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(picked, unpicked):
            if not unpicked:
                res.append(picked.copy())
                return

            for i, num in enumerate(unpicked):
                picked.append(num)
                backtrack(
                    picked, unpicked[:i] + unpicked[i + 1 :]
                )  # [], [1,2,3] -> [1], [2, 3] or [2], [1,3] or [3], [1,2]
                picked.pop()

        res = []
        backtrack([], nums)
        return res
