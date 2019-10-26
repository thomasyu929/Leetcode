class Solution:

    #1

    def maxSubArray(self, nums: List[int]) -> int:
        res, con = float('-inf'), 0
        for i in nums:
            con = max(i, i + con)
            res = max(con, res)
        return res
    
    #2
    
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return nums[i]

    #3  divide and conquer approach


    # shows that Time Limit Exceeded
    
    def maxSubArray(self, nums):
        if not nums:
            return 0
        return self.divideConquer(nums, 0, len(nums)-1)
    def divideConquer(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = left + right // 2
        ltan = self.divideConquer(nums, left, mid)
        rtan = self.divideConquer(nums, mid+1, right)
        lmax = nums[mid]
        rmax = nums[mid+1]
        temp = 0
        i = mid 
        while i >= left:
            temp += nums[i]
            if temp > lmax:
                lmax = temp
        temp = 0
        for i in range(mid+1, right):
            temp += nums[i]
            if temp > rmax:
                rmax = temp
        return max(max(ltan,rtan), lmax+rmax)

            
