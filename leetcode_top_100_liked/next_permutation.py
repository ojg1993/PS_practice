class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                idx = i - 1
                break

        if idx == -1:
            nums.reverse()

        else:
            for i in range(len(nums) - 1, idx, -1):
                if nums[i] > nums[idx]:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    nums[idx + 1:] = reversed(nums[idx + 1:])
                    break