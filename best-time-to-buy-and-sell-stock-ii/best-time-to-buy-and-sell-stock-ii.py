class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while(i < len(prices) - 1):
            # Loop checks if we are not yet at a valley
            while (i < len(prices) - 1 and prices[i] >= prices[i + 1]):
                i += 1
            valley = prices[i] # Marking the current valley
            # Loop checking that we are still in a valley
            while(i < len(prices) - 1 and prices[i] <= prices[i + 1]):
                i += 1
            peak = prices[i] # Marking our peak
            maxprofit += peak - valley
        return maxprofit
        