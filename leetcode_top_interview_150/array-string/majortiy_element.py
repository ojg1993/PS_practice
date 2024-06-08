class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {key: 0 for key in nums}

        for num in nums:
            num_dict[num] += 1

        return max(num_dict, key=num_dict.get)
