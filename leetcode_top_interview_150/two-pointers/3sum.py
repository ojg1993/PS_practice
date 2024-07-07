class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = set()
        # nums.sort()

        # for i in range(len(nums)-2):
        #     l, r = i+1, len(nums)-1

        #     while l < r:
        #         tot = nums[i] + nums[l] + nums[r]

        #         i tot < f0:
        #             l += 1
        #         elif tot > 0:
        #             r -= 1
        #         else:
        #             res.add((nums[i],nums[l],nums[r]))
        #             l += 1
        #             r -= 1
        # return [list(r) for r in res]

        h = dict()
        res = set()
        for i, val in enumerate(nums):
            h[val] = i

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = -nums[i] - nums[j]
                if target in h and h[target] != i and h[target] != j:
                    res.add(tuple(sorted([nums[i], nums[j], target])))
        return res
