class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        # time limit exceeded
        
#         dp = [list(range(1, n+1))]
#         count = 0
#         while count+1 != k:
#             nums = dp[-1]
#             i, j = n-1, n-1
#             while i > 0 and nums[i-1] >= nums[i]:
#                 i -= 1
#             if i > 0:
#                 while nums[j] <= nums[i-1]:
#                     j -= 1
#                 nums[i-1], nums[j] = nums[j], nums[i-1]
#                 nums[i:] = list(reversed(nums[i:]))
#             else:
#                 return nums.reverse()
#             count += 1
#             dp.append(nums)
#         # print(dp[-1])
#         res = 0
#         for i in dp[-1]:
#             res = res*10 + i 
#         return str(res)
        
        # regular
        res = ""
        nums = "123456789"
        k = k-1
        fac = [1]*n
        for i in range(1, n):
            fac[i] = fac[i-1] * (i)
        for i in range(n, 0, -1):
            a = k // fac[i-1]
            k %= fac[i-1]
            res += nums[a]
            nums = nums.replace(nums[a], "")
        return res
            
            
            
        
            