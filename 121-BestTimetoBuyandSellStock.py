class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                continue
            max_profit = max(prices[i] - min_price, max_profit)
        return max_profit 