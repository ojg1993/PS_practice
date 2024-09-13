class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        nums to bit = 2^n-1
        10 10 01
        res = 10 -> 00 -> 01

        4 1 2 1 2
        res = 100 -> 101 -> 111 -> 110 -> 100

        1 2 1 2 4
        res = 01 -> 11 > 10 > 00 > 100
        """
        res = nums[0]

        for num in nums[1:]:
            res ^= num
        return res
