class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = {}

        for idx, val in enumerate(nums):
            if val in hash_map and idx - hash_map[val] <= k:
                return True
            hash_map[val] = idx
        return False
