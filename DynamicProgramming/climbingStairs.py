class Solution:
    def climbStairs(self, n: int) -> int:
        
        # 1
        
        # dp = [1] + [0]*(n)
        # for i in range(1, n+1):
        #     for n in range(1, 3):
        #         if n > i: continue
        #         dp[i] += dp[i-n]
        # return dp[-1]
        
        # 2
        
        # if n <= 1: return 1
        # dp = [1] + [2] + [0]*(n-2)
        # for i in range(2, n):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[-1]
        
        # 3
        
        # if n <= 1: return 1
        # a, b = 1, 1
        # while n:
        #     b += a
        #     a = b - a
        #     n -= 1
        # return a
        
        # 4
        
        memo = [0]*(n+1)
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n <= 1: return 1
        if memo[n] > 0: return memo[n]
        memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
            
        
        