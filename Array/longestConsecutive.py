class Solution:
    def longestConsecutive(self, nums):

        '''
        algorithm should run in O(n) complexity
        考虑了不允许重复值出现的情况
        '''
        # temp, count, mx= float('inf'), 0, 0
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == temp + 1:
        #         temp = nums[i]
        #         count += 1
        #     elif nums[i] == temp and count == 1:
        #         continue
        #     else:
        #         mx = max(mx, count)
        #         count = 1
        #         temp = nums[i]
        # return max(mx, count)

        # temp, count, mx = float('inf'), 0, 0
        # nums = list(set(nums))
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == temp + 1:
        #         temp = nums[i]
        #         count += 1
        #     else:
        #         mx = max(mx, count)
        #         count = 1
        #         temp = nums [i]
        # return max(mx, count)

        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best