class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0

        for i in prices:
            maxProfit = max(maxProfit, i - minBuy)
            minBuy = min(minBuy, i)
        return maxProfit