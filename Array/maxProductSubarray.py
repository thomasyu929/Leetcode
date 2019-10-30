class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        bnums = nums[::-1]
        
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            bnums[i] *= bnums[i-1] or 1
        return max(nums + bnums)
        