class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof, i = 0, 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                prof = prof + prices[i] - prices[i-1]
        return prof

    # one-line solution but not better
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))