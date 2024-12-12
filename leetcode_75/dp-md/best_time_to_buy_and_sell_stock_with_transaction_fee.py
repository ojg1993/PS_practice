class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, profit = prices[0], 0

        for sell in prices[1:]:
            buy = min(buy, sell - profit)
            profit = max(profit, sell - buy - fee)
        return profit
