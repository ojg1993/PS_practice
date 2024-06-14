class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curJump = maxJump = 0
        cnt = 0

        for i in range(len(nums) - 1):
            maxJump = max(maxJump, i + nums[i])

            if maxJump >= len(nums) - 1:
                cnt += 1
                break

            if i == curJump:
                curJump = maxJump
                cnt += 1

        return cnt
