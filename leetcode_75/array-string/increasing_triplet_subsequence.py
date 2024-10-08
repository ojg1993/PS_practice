class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = mid = float('inf')

        for right in nums:
            if right <= left:
                left = right
            elif right <= mid:
                mid = right
            else:
                return True
        return False
