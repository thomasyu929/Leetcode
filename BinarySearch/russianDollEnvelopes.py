class Solution:
    
    # dp TLE
    
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         if not envelopes: return 0
#         envelopes.sort()
#         dp = [1]*len(envelopes)
#         for i in range(len(envelopes)):
#             for j in range(i+1):
#                 if envelopes[i][1] > envelopes[j][1] and envelopes[i][0] > envelopes[j][0]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)
    
    # binary search     LIS
    
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        res = []
        envelopes.sort(key = lambda key : (key[0], -key[1]))
        for i in range(len(envelopes)):
            left, right = 0, len(res)
            while left < right:
                mid = left + (right-left)//2
                if res[mid] < envelopes[i][1]:
                    left = mid + 1
                else:
                    right = mid
            if right == len(res): res.append(envelopes[i][1])
            else: res[right] = envelopes[i][1]
        return len(res)
            