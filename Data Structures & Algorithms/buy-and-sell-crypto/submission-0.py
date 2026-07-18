class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best_profit = 0

        for price in prices:
            lowest = min(lowest, price)
            profit = price - lowest
            if profit > best_profit:
                best_profit = profit

        return best_profit