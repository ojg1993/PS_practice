class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 in nums:
                continue

            seq = 1

            while num + seq in nums:
                seq += 1
            res = max(res, seq)
        return res
