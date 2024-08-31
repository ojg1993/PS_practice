class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        case 1: max intervals in the middle of array
        case 2: max intervals in circular array
        case 3: negative value intervals
        """
        g_max = l_max = g_min = l_min = tot = nums[0]

        for num in nums[1:]:
            tot += num
            l_max = max(l_max + num, num)
            g_max = max(g_max, l_max)
            l_min = min(l_min + num, num)
            g_min = min(g_min, l_min)

        return max(g_max, tot - g_min) if g_max > 0 else g_max
