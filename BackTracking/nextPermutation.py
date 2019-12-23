class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 1
        
        # ti = -1
        # t = float('inf')
        # for i in range(len(nums)-1, 0, -1):
        #     if nums[i-1] < nums[i]:
        #         for num in nums[i:]:
        #             if num > nums[i-1]:
        #                 t = min(t, num)
        #         for j in range(i, len(nums)):
        #             if nums[j] == t:
        #                 ti = max(ti, j)
        #         nums[ti], nums[i-1] = nums[i-1], nums[ti]
        #         nums[i:] = list(reversed(nums[i:]))
        #         return
        # nums.reverse()
        
        # 2
        
        # ti = -1
        # for i in range(len(nums)-1, 0, -1):
        #     if nums[i-1] < nums[i]:
        #         for j in range(len(nums)-1, i-1, -1):
        #             if nums[j] > nums[i-1]:
        #                 ti = j
        #                 break
        #         nums[ti], nums[i-1] = nums[i-1], nums[ti]
        #         nums[i:] = list(reversed(nums[i:]))
        #         return
        # nums.reverse()
        
        # 3
        
        i = len(nums) - 1
        j = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i > 0:
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[j], nums[i-1] = nums[i-1], nums[j]
            nums[i:] = list(reversed(nums[i:]))
        else:
            nums.reverse() 



if __name__ == "__main__":
    cl = Solution()
    nums = [1,2,3]
    print(cl.nextPermutation(nums))