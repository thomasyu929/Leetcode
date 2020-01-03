class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # stupid
        
#         nums.sort()
#         return nums[0]  
        
        # 1
    
#         left, right = 0, len(nums)-1
#         mid = left + (right-left)//2
#         if nums[mid] > nums[right]:
#             target = nums[left]
#             nums = nums[mid+1:]
#         else:
#             target = nums[mid]
#             nums = nums[:mid]
#         for i in nums:
#             target = min(target, i)
#         return target

        # 2 best
    
#         left, right = 0, len(nums)-1
#         while left < right:
#             mid = left + (right-left)//2
#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid
#         return nums[left]  # or right
    
        # divide conquer
        
        return self.findMini(nums, 0, len(nums)-1)
        
    def findMini(self, nums, start, end):
        if nums[start] <= nums[end]: return nums[start]
        mid = start + (end-start) // 2
        return min(self.findMini(nums, start, mid), self.findMini(nums, mid+1, end))
        