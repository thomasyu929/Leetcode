class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)
        fd = nums[1] - nums[0]
        count = 1 + (fd != 0)
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff * fd <= 0 and diff != 0:
                count += 1
                fd = diff
        return count