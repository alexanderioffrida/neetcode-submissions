class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxPro = 0
        
        for i in range(len(prices)):
            minBuy = min(minBuy, prices[i])
            maxPro = max(maxPro, prices[i] - minBuy)
        return maxPro