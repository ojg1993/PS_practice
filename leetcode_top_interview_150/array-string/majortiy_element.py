class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(1) space, O(n) time
        cnt = 1
        res = nums[0]

        for cur in nums[1:]:
            cnt += 1 if res == cur else -1
            if cnt < 1:
                res = cur
                cnt = 1
        return res

        # hash: O(n) space, O(n) time
        # num_dict = {key: 0 for key in nums}

        # for num in nums:
        #     num_dict[num] += 1

        # return max(num_dict, key=num_dict.get)
