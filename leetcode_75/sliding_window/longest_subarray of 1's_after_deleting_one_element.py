class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        flag, left, res = 1, 0, 0

        for right in range(len(nums)):
            if not nums[right]:
                flag -= 1
            while flag < 0:
                if not nums[left]:
                    flag += 1
                left += 1
            res = max(res, right - left)

        return res
