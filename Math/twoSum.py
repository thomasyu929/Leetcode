class Solution:
    
    # brute force
    '''
    def twoSum(self, nums, target):
        for i in range(len(nums)):
             for j in range(len(nums))[i+1:]:        # not use the same element twice
                if nums[i] + nums[j] == target:
                    return i,j
    '''
        
    
    # hash map
    
    def twoSum(self, nums, target):
        m = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in m:
                return i, m[x]
            else:
                m[n] = i


if __name__ == "__main__":
    cl = Solution()
    nums = [2,7,11,15]
    target = 9
    print(cl.twoSum(nums, target))