class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        idx = 0

        while idx < len(nums):
            s = e = idx
            while e + 1 < len(nums) and nums[e] + 1 == nums[e + 1]:
                e += 1

            if s == e:
                res.append(f"{nums[s]}")
            else:
                res.append(f"{nums[s]}->{nums[e]}")
            idx = e + 1
        return res
