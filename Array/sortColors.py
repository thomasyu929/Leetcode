class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        
        '''
        easy, put 0 in front, and put 2 in the behind.
        finally it will be sorted.
        '''

        i, low, high = 0, 0, len(nums)-1
        for i in range(len(nums)):
            while nums[i] == 2 and i < high:
                temp = nums[i]
                nums[i] = nums[low]
                nums[low] = nums[i]
                high -= 1
            while nums[i] == 0 and i > low:
                temp = nums[i]
                nums[i] = nums[low]
                nums[low] = temp
                low += 1