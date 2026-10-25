class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        current_min = max(prices)
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < current_min:
                current_min = prices[i]

            current_profit = prices[i] - current_min
            if current_profit > max_profit:
                max_profit = current_profit

        return max(0, max_profit)