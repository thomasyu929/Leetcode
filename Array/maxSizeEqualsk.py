class Solution:
    def maxSubArrayLen(self, nums, k):
        sum, res = 0, 0
        m = {}
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                res = i + 1
            elif sum - k in m:
                res = max(res, i - m[sum-k])
            if sum not in m:
                m[sum] = i
        return res