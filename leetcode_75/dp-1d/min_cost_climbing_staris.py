class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        left, right = cost[0], cost[1]

        for c in cost[2:]:
            left, right = right, c + min(right, left)
        return min(left, right)
