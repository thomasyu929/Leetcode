class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 在fwd[]和bwd[]的基础上进行 空间优化 使用临时变量right

        res = [0] * len(nums)
        res[0] = 1
        
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
            
        right = 1
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res