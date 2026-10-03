class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        sell = 0
        lowest = prices[0]
        for i in range(len(prices)-1):
            if prices[i] > prices[i+1]:
                profit = max(0,profit)
            else:
                lowest = min(prices[i],lowest)
                buy = prices[i+1]

                profit = max(buy - lowest, profit)

        return profit
