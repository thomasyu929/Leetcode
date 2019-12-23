class Solution:
    # def numTrees(self, n: int) -> int:
    #     dp = [0]*(n+1)
    #     dp[0] = dp[1] = 1
    #     for i in range(2, n+1):
    #         for j in range(i):
    #             dp[i] += dp[j] * dp[i-j-1]
    #     return dp[-1]

    # def numTrees(self, n: int) -> int:
    #     res = 0
    #     a, b = 1, 1
    #     for i in range(n+1, 2*n+1):
    #         a *= i
    #     for j in range(1, n+1):
    #         b *= j
    #     print(a, b)
    #     res = (a//b)//(n+1)
    #     return res

    def numTrees(self, n):
        import math
        return int(math.factorial(2*n) / (math.factorial(n+1) * math.factorial(n)))


if __name__ == "__main__":
    cl = Solution()
    n = 7
    print(cl.numTrees(n))
