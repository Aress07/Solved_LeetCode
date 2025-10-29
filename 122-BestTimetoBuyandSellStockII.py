class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                continue
            elif (prices[i] - min_price) > 0:
                max_profit += prices[i] - min_price
                min_price = prices[i]

        return max_profit