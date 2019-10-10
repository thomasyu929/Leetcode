class Solution:
    def maxProfit(self, prices):
        buy = float('-inf')
        cooldown = float('-inf')
        sell = 0
        for p in prices:
            buy = max(buy, sell - p)
            sell = max(sell, cooldown)
            cooldown = buy + p
        return max(sell, cooldown)