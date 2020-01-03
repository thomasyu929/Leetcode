class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
#         if not nums: return 0
#         dp = [1]*len(nums)
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j]+1)
#         return max(dp)
    
        res = []
        for i in range(len(nums)):
            left, right = 0, len(res)
            while left < right:
                mid = left + (right-left)//2
                if res[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if right >= len(res):
                res.append(nums[i])
            else:
                res[right] = nums[i]
        return len(res)