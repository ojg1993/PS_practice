class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        base = 1
        for i in range(len(nums)):
            if nums[i]==base:
                base += 1
        
        return base