class Solution:
    
    # brute force       time limit exceeded
    
    # def maxProfit(self, prices):
    #     buy, sell, maxprof = 0, 0, 0
    #     for buy in range(len(prices)):
    #         for sell in range(buy, len(prices)):
    #             prof = prices[sell] - prices[buy]
    #             if prof > maxprof:
    #                 maxprof = prof
    #     return maxprof
    
    # Kandane's Algorthim

    # def maxProfit(self, prices):
    #     i, maxprof, prof = 0, 0, 0
    #     for i in range(1, len(prices)):
    #         prof = prof + prices[i]-prices[i-1]
    #         prof = max(0, prof)
    #         maxprof = max(maxprof,prof)
    #     return maxprof

    # another way

    def maxProfit(self, prices):
        low = float('inf')  # Representing positive infinity
        prof = 0
        for i in prices:
            prof = max(prof, i - low)
            low = min(low, i)
        return prof