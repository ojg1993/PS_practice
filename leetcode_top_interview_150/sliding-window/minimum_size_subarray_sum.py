class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        res = 10**9
        tot = nums[r]

        while r < len(nums):
            if tot >= target:
                res = min(res, r - l + 1)
                tot -= nums[l]
                l += 1
            else:
                r += 1
                if r == len(nums):
                    break
                tot += nums[r]

        return res if res < 10**9 else 0
