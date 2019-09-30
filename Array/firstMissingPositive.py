class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        count = 0
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 0
                count += 1
        nums = nums[0:len(nums)-count] 
        nums = list(set(nums))
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]-1:
                return i + 1
        return len(nums) + 1