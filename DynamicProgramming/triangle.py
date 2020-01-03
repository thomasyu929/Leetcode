class Solution:
    
    # use original array
    
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         if not triangle or len(triangle[0]) == 0: return 0
#         if len(triangle) == 1: return min(triangle[0])
#         for i in range(1, len(triangle)):
#             triangle[i][0] += triangle[i-1][0]
#             triangle[i][-1] += triangle[i-1][-1]
#             for j in range(1, len(triangle[i])-1):
#                 triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
#         return min(triangle[-1])
    
    # use last triangle row as dp arrary, bottom-up calculate minimum path
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or len(triangle[0]) == 0: return 0
        if len(triangle) == 1: return min(triangle[0])
        dp = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
    