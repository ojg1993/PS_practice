class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        r1, r2 = nums[0], max(nums[0], nums[1])

        for money in nums[2:]:
            choice = max(money+r1, r2)
            r1, r2 = r2, choice
        return max(r1, r2)
