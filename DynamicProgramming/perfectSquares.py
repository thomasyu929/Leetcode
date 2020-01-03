class Solution:
    
    # dp

    # def numSquares(self, n: int) -> int:
    #     dp = [0]
    #     while len(dp) <= n:
    #         i = 1
    #         val = float('inf')
    #         while i*i <= len(dp):
    #             val = min(val, dp[len(dp) - i*i]+1)
    #             i += 1
    #         dp.append(val)
    #     return dp[n]

    # dp

    # def numSquares(self, n: int) -> int:
    #     dp = [0] + [float('inf')]*n
    #     for i in range(1, n+1):
    #         dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
    #     return dp[n]
    
    # math 

    def numSquares(self, n: int) -> int:
        from math import sqrt
        x = int(sqrt(n))
        if x * x == n:
            return 1 
        while n % 4 == 0: n //= 4
        if n % 8 == 7: return 4
        for a in range(int(n**0.5)+1):
            b = int(sqrt(n-a*a))
            if a*a + b*b == n:
                return 2
        return 3

if __name__ == "__main__":
    cl = Solution()
    n = 11
    print(cl.numSquares(n))


                