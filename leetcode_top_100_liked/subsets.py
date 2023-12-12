class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur, subset):
            if cur >= len(nums):
                res.append(subset)
                return

            backtrack(cur + 1, subset + [nums[cur]])
            backtrack(cur + 1, subset)

        res = []
        backtrack(0, [])
        return res