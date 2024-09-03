class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        0 and len(nums)-1 can be peak, if idx reaches either, return idx
        there can be multiple peaks,  return any of peak idx
        return peak value
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m
