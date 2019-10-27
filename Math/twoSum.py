class Solution:
    
    # brute force
    '''
    def twoSum(self, nums, target):
        for i in range(len(nums)):
             for j in range(len(nums))[i+1:]:        # not use the same element twice
                if nums[i] + nums[j] == target:
                    return i,j
    '''
        
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i