class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(nums, arr, tot):
            if tot == target:
                res.append(arr)
            if tot >= target:
                return
            else:
                for i in range(len(nums)):
                    backtrack(nums[i:], arr + [nums[i]], tot + nums[i])

        backtrack(candidates, [], 0)

        return res