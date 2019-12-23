class Solution:
    
    # iteration
    
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         res = [[]]
#         nums.sort()
#         last = float('-inf')
#         for num in nums:
#             if last != num:
#                 last = num
#                 l = len(res)
            
#             res += [[num] + res[j] for j in range(len(res) - l, len(res))]
                
#         return res
        # remove duplicate elements
        # return list(set([tuple(i) for i in res]) )
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.helper(nums, [], 0, res)
        return res
        
    def helper(self, nums, path, index, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]: 
                continue
            self.helper(nums, path + [nums[i]], i+1, res)
        