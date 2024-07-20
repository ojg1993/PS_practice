class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for idx, val in enumerate(nums):
            complement = target - val
            if complement in hash_map:
                return idx, hash_map[complement]
            hash_map[val] = idx
