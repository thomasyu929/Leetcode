class Solution:
    # def uniquePathsWithObstacles(self, obstacleGrid):
    #     if not obstacleGrid or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:
    #         return 0
    #     m = len(obstacleGrid)
    #     n = len(obstacleGrid[0])
    #     temp = [0]*(n+1)
    #     dp = []
    #     for _ in range(m+1):
    #         dp.append(temp[:])
    #     dp[0][1] = 1
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if obstacleGrid[i-1][j-1] != 1:
    #                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #     return dp[m][n]

    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0]*n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[n-1]
                
    
                
if __name__ == "__main__":
    cl = Solution()
    obstacleGrid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
        ]
    print(cl.uniquePathsWithObstacles(obstacleGrid))