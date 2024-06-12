class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # maxJump = 0
        # for i in range(len(nums)):
        #     if i > maxJump:
        #         return False
        #     maxJump = max(maxJump, i + nums[i])
        # return True

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
