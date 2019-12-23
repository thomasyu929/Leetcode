
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

    # slide window

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s: return 0
        left, right, x = 0, 0, len(nums)+1
        res = 0
        while right < len(nums):
            while right < len(nums) and res < s:
                res += nums[right]
                right += 1
            while left < right and res >= s:
                x = min(x, right - left)
                res -= nums[left]
                left += 1
        return x
        