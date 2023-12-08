# from itertools import permutations
#
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         for p in permutations(nums, len(nums)):
#             res.append(p)
#         return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(picked, unpicked):
            if not unpicked:
                res.append(picked)
                return
            for i, num in enumerate(unpicked):
                dfs(picked + [num], unpicked[:i] + unpicked[i + 1:])

        dfs([], nums)

        return res