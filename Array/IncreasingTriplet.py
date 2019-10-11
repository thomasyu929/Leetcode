class Solution:
    def increasingTriplet(self, nums):
        if not nums:
            return False
        
        n, m1, m2 = 0, float('-inf'), float('-inf')
        for n in nums:
            if m1 >= n:
                m1 = n
            elif m2 >= n:
                m2 = n
            else:
                return True
        return False