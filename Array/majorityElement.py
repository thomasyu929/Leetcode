class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # from collections import Counter
        # c = Counter()
        # l = len(nums)
        # for i in nums:
        #     c[i] += 1
        # for j in nums:
        #     if c[j] > l/2:
        #         return j
        nums.sort()
        return nums[(len(nums)//2)]