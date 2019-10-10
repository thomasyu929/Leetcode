import sys
class Solution:
    def maxProfit(self, prices):
        oneBuy = twoBuy = sys.maxsize
        oneProf = twoProf = 0
        for i in prices:
            oneBuy = min(oneBuy, i)
            oneProf = max(oneProf, i - oneBuy)

            # buy second stock just need to pay the part which is except profit you earn
            twoBuy = min(twoBuy, i - oneProf)
            
            twoProf = max(twoProf, p - twoBuy)
        return twoProf