class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = dict()

        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1

        for key in res:
            if res[key] == 1:
                return key