class Solution:
    def wiggSort(self, nums):
        nums.sort()
        if len(nums) <= 2:
            return nums
        for i in range(2, len(nums), 2):
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
        return nums

