class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k <= 0:
            return False
        if t == 0 and len(set(nums)) == len(nums):
            return False
        for i in range(len(nums)-1):
            for j in range(i+1, min(i+1+k, len(nums))):
                if j - i <= k and abs(nums[j]-nums[i]) <= t:
                    return True
        return False