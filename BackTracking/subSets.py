class Solution:
    
    # iteration
    
    def subsets(self, nums):
        #  res is 2D array
        res = [[]]
        ans =[]
        nums.sort()
        for num in nums:
            path = []
            for i in res:
                s = i + [num]
                path.append(s)
                # if len(s) == k:
                #     ans.append(s)
            res += path
        return res
        
    # recursive
    
    # def subsets(self, nums):
    #     res = []
    #     self.helper(nums, 0, res, [])
    #     return res
        
    # def helper(self, nums, index, res, path):
    #     res.append(path)
    #     for i in range(index, len(nums)):
    #         self.helper(nums, i+1, res, path+[nums[i]])

if __name__ == "__main__":
    cl = Solution()
    nums = [1,2,3]
    print(cl.subsets(nums))