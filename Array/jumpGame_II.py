class Solution:
    # def jump(self, nums):
    #     res, last, i, cur = 0, 0, 0, 0
    #     n = len(nums)
    #     for i in range(n-1):
    #         cur = max(cur, i+nums[i])
    #         if i == last:
    #             res += 1
    #             last = cur
    #             if cur >= n-1
    #                 break
    #     return res

    # another way

        res, last, i, cur = 0, 0, 0, 0
        n = len(nums)
        while cur < n-1:
            res += 1
            pre = cur
            while i <= pre:
                cur = max(cur, i + nums[i])
                i += 1
            if pre == cur:
                return -1
        return res