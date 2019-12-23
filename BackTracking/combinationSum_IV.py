class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if num > i: break
                else:
                    dp[i] += dp[i-num]
        # dp[n] = dp[n-1] + dp[n-2] + ... + dp[1] + dp[0]             
        
        return dp[-1]

    # follow-up

    def combinationSum4(self, nums, target, maxlength):
        
        from collections import defaultdict
        memo = defaultdict[int]
        return self.helper(target, nums, maxlength)
    
    def helper(self, target, nums, l):
        if target == 0: return 1
        if l == 0: return 0
        if (target, l) in memo:
            return memo[(target, l)]
        res = 0
        for num in nums:
            res += self.helper(target-num, nums, l-1)
        memo[(target, l)] = res
        return res
            