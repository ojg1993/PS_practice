class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy, sell = 0, 1

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit += prices[sell] - prices[buy]
            buy += 1
            sell += 1

        return profit
