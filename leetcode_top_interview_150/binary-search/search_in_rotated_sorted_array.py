class Solution:
    def search(self, nums, target: int) -> int:
        """
        1. nums can be rotated k times
        """

        l, r = 0 , len(nums)-1

        while l <= r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m-1
        idx = l

        if not idx:
            l, r = 0, len(nums)-1
        elif nums[0] < target:
            l =