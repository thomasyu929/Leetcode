class Solution:
    def minSubArrayLen(self, s, nums):
        total, left, res = 0, 0, float('inf')
        for i in range(len(nums)):
            total += nums[i]
            while left <= i and total >= s:
                res = min(res, i-left+1)
                total -= nums[left]
                left += 1
        if res == float('inf'):
            return 0
        else:
            return res