class Solution:
    def maxProfit(self, k, prices):
        if not prices:
            return 0 
        if k >= len(prices) // 2:    # each transaction needs two days to finish
            return sum(x-y for x, y in zip(prices[1:], prices[:-1]) if x > y)

        prof = [0]*len(prices)
        for j in range(k):

        # j表示可进行最大交易次数，profs[i]储存i天之前的j次交易的最大利润

            preprof = 0
            for i in range(1, len(prices)):
                prof = prices[i] - prices[i-1]
                preprof = max(preprof + prof, profs[i])
                profs[i] = max(profs[i-1], preprof)
                
        return profs[-1]