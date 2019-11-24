class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        x = float('inf')
        res = 0
        nums.sort()
        for i in range(len(nums)-2):
            goal = target - nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                if abs(nums[left] + nums[right] - goal) < x:
                    res = nums[left] + nums[right] + nums[i]
                    x = abs(nums[left] + nums[right] - goal)
                if nums[left] + nums[right] < goal:
                    left += 1
                elif nums[left] + nums[right] > goal:
                    right -= 1
                else:
                    return res
        return res

if __name__ == "__main__":
    cl = Solution()
    nums = [1,1,1,0]
    target = -100
    print(cl.threeSumClosest(nums, target))