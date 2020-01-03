class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # stupid O(n) or sort O(nlogn)
        
#         res = float('inf')
#         for i in nums:
#             res = min(res, i)
#         return res
        
        # divide and conquer
        
#         return self.findMini(nums, 0, len(nums)-1)
    
#     def findMini(self, nums, start, end):
#         if start == end: return nums[start]
#         if nums[start] < nums[end]: return nums[start]
#         mid = start + (end-start)//2
#         return min(self.findMini(nums, start, mid), self.findMini(nums, mid+1, end))
    
        # binary search
        
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]
    