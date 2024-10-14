class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])
        res = cur / k

        for i in range(k, len(nums)):
            cur = cur - nums[i-k] + nums[i]
            res = max(res, cur/k)
        return res
