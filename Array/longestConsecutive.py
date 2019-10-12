class Solution:
    def longestConsecutive(self, nums):

        '''
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
        
        temp, count, mx = float('inf'), 0, 0
        nums = list(set(nums))
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == temp + 1:
                temp = nums[i]
                count += 1
            else:
                mx = max(mx, count)
                count = 1
                temp = nums [i]
        return max(mx, count)