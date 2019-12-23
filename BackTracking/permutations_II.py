class Solution:
    
    # slow solution
    
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         self.helper(nums, res, 0)
#         return res
        
#     def helper(self, nums, res, index):
#         if index >= len(nums) and nums not in res:
#             res.append(nums)
#         for i in range(index, len(nums)):
#             newnums = nums[:]
#             newnums[i], newnums[index] = newnums[index], newnums[i]
#             self.helper(newnums, res, index+1)

    
    # swap solution
    
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         self.helper(nums, res, 0)
#         return res
        
#     def helper(self, nums, res, index):
#         if index >= len(nums) and nums not in res:
#             res.append(nums)
#         for i in range(index, len(nums)):
#             if i != index and nums[i] == nums[index]:
#                 continue
#             newnums = nums[:]
#             newnums[i], newnums[index] = newnums[index], newnums[i]
#             self.helper(newnums, res, index+1)
    
    # visited record 0 & 1 recursive
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        visited = [0]*len(nums)
        self.helper(nums, res, [], visited)
        return res
    
    def helper(self, nums, res, path, visited):
        if len(path) == len(nums):
            return res.append(path)
        for i in range(len(nums)):
            if visited[i] == 1: continue
            if i > 0 and nums[i] == nums[i-1] and visited[i-1] == 0:
                continue
            visited[i] = 1
            self.helper(nums, res, path+[nums[i]], visited)
            visited[i] = 0
        
    