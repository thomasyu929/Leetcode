class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: return 0
        if len(grid) == 1: return sum(grid[0])
        m = len(grid)
        n = len(grid[0])
        dp = grid[:]
        for i in range(1, n):
            dp[0][i] += dp[0][i-1]
        for i in range(1, m):
            dp[i][0] += dp[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]

if __name__ == "__main__":
    cl = Solution()
    grid = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
            ]
    print(cl.minPathSum(grid))