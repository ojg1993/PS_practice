class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        l, r = 0, len(height) - 1

        while l < r:
            water = (r - l) * min(height[l], height[r])
            max_water = max(max_water, water)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water
