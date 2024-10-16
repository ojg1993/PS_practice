class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, res = 0, 0

        for right in range(len(nums)):
            if not nums[right]:
                k -= 1
            while k < 0:
                if not nums[left]:
                    k += 1
                left += 1
            width = right - left + 1
            res = max(res, width)

        return res
