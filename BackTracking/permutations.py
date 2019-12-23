class Solution:
    
    # recursive
    
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         visited = [0] * len(nums)
#         self.helper(nums, visited, [], res)
#         return res
        
#     def helper(self, nums, visited, path, res):
#         if len(path) == len(nums):
#             return res.append(path)
#         for i in range(len(nums)):
#             if visited[i] == 1:
#                 continue
#             visited[i] = 1
#             self.helper(nums, visited, path+[nums[i]], res)
#             visited[i] = 0
      
    # slice recursive
    
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         self.helper(nums, [], res)
#         return res
    
#     def helper(self, nums, path, res):
#         if len(path) == len(nums):
#             res.append(path)
#             return
#         for i in range(len(nums)):
#             self.helper(nums[:i]+nums[i+1:], path+[nums[i]], res)

    # swap recursive
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, res)
        return res
    
    def helper(self, nums, index, res):
        if index >= len(nums):
            res.append(nums)
        for i in range(index, len(nums)):
            numss = nums[:]
            numss[i], numss[index] = numss[index], numss[i]
            self.helper(numss, index+1, res)
    
    # swap iteration
    
#     def permute(self, nums):
#         res = [nums]
#         for i in range(len(nums)-1):
#             path = []
#             for a in res:
#                 for j in range(i+1, len(nums)):
#                     newnums = a[:]
#                     newnums[i], newnums[j] = newnums[j], newnums[i]
#                     path.append(newnums)
#             res += path
            
#         return res
                    
        
 
