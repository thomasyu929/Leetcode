class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        c1, c2, cd1, cd2 = 0, 0, 0, 1
        final = []
        for n in nums:
            if n == cd1:
                c1 += 1
            elif n == cd2:
                c2 += 1
            elif c1 == 0:
                cd1, c1 = n, 1
            elif c2 == 0:
                cd2, c2 = n, 1
            else:
                c1 -= 1
                c2 -= 1
        # return [n for n in (cd1, cd2)
        #             if nums.count(n) > len(nums) // 3] 
        for n in (cd1, cd2):
            if nums.count(n) > len(nums) // 3:
                final += [n]
        return final