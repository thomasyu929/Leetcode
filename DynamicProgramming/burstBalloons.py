class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        nums = [1] + nums + [1]
        # dp = [[0]*(n+2)]*(n+2)
        dp = [[0]*(n+2) for x in range(n+2)]
        for l in range(n):
            for i in range(1,n-l+1):
                j = i + l
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], ((nums[i-1]*nums[k]*nums[j+1]) + dp[i][k-1] + dp[k+1][j]))
        return dp[1][n]
        

if __name__ == "__main__":
    cl = Solution()
    nums = [3,1,5,8]
    print(cl.maxCoins(nums))