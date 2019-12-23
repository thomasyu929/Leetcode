class Solution:
    
    # dp every column in each row
    
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [1] + [0]*(n-1)
#         for i in range(m):
#             for j in range(1, n):
#                 dp[j] += dp[j-1]
#         return dp[-1]
    
    # m+n-2
    
    def uniquePaths(self, m: int, n: int) -> int:
        demon = 1
        num = 1
        small = min(m, n)
        # for i in range(m+n-small, m+n-1):
        #     num *= i
        # for i in range(1, small):
        #     demon *= i
        for i in range(1, small):
            num *= m+n-1-i
            demon *= i
        return num // demon  
    
        
        