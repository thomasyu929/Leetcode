class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # 0 
        
        # if not nums or nums[0] >= target: return 0
        # if nums[-1] < target: return len(nums)
        # left, right = 0, len(nums)-1
        # while left < right:
        #     mid = left + (right-left+1) // 2
        #     if nums[mid] > target:
        #         if nums[mid-1] < target:
        #             return mid
        #         right = mid
        #     elif nums[mid] < target:
        #         left = mid
        #     else:
        #         return mid
        # return mid
        
        # 1 easy way but not the best
        
#         for i in range(len(nums)):
#             if nums[i] >= target: return i
#         return len(nums)
    
        # 2 binary search
        
        if nums[-1] < target: return len(nums)
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return right