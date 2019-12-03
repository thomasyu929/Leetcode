class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                x = target - nums[i] - nums[j]
                left, right = j+1, len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == x:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left+1] == nums[left]:
                            left += 1
                        while left < right and nums[right-1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > x:
                        right -= 1
                    else:
                        left += 1
        return res

if __name__ == "__main__":
    cl = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(cl.fourSum(nums, target))