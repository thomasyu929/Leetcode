class Solution:
    def containsNearbyDuplicate(self, nums, k):
        i, v = 0, 0
        dit = {}
        for i, v in enumerate(nums):
            if v in dit and i - dit[v] <= k:
                return True
            else:
                dit[v] = i
        return False