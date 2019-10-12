class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        mx = 0
        if not nums or len(nums)==1:
            return 0
        nums.sort()
        # for i in range(len(nums)-1):
        mx = max(list(map(lambda x: x[1]-x[0], zip(nums[:-1],nums[1:]))))
        return mx