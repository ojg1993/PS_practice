class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        global_max = local_max = nums[0]

        for num in nums[1:]:
            local_max = max(num, local_max + num)
            global_max = max(global_max, local_max)

        return global_max
