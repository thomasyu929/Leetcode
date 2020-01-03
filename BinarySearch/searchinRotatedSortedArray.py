class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''
        we can find in the array whatever pivot is, 
        it must ordered in first half or second half
        '''
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target: return mid
            elif nums[mid] < nums[right]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1