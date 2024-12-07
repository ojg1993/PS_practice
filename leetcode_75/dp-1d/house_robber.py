class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        prev, cur = nums[0], max(nums[0], nums[1])

        for num in nums[2:]:
            nxt = max(prev + num, cur)
            prev, cur = cur, nxt
        return cur
