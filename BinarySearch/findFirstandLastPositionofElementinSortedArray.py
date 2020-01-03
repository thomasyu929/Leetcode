class Solution:
    def searchRange(self, nums, target):
        res = [-1, -1]
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if right == len(nums) or nums[right] != target: return res
        res[0] = right
        print(left)
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        print(left, right)
        res[1] = right-1
        return res

if __name__ == "__main__":
    cl = Solution()
    target = 8
    nums = [1, 2, 8, 8, 9, 9]
    print(cl.searchRange(nums, target))