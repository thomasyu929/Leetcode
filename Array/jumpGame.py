class Solution:
    def canJump(self, nums):
        i, j = 0, 0
        for i in range(len(nums)):
            if (j >= len(nums)-1) or (i >j):    # 如果当前坐标reach到不了，break
                break
            else:
                j = max(i + nums[i],j)
        return j >= len(nums)-1