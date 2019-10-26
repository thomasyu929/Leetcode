class Solution:
    def moveZeros(self, nums):
        i, nzero = 0, 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[nzero]
                nums[nzero] = temp
                nzero += 1