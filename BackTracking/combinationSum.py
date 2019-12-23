class Solution:
    
    # recursive

    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     res = []
    #     self.helper(candidates, target, 0, [], res)
    #     return res
    
    # def helper(self, candidates, target, index, path, res):
    #     if target < 0: return
    #     if target == 0: return res.append(path)
    #     for i in range(index, len(candidates)):
    #         self.helper(candidates, target - candidates[i], i, path+[candidates[i]], res)
    
    # iteration
    
    def combinationSum(self, candidates, target):
        dp = []
        candidates.sort()
        for i in range(1, target+1):
            cur = []
            for num in candidates:
                if num > i: break
                if num == i: 
                    cur.append([num])
                    break
                for a in dp[i - num - 1]:
                    if num >= a[-1]: 
                        cur.append(a + [num])
            dp.append(cur)
        return dp[target-1]



if __name__ == "__main__":
    cl = Solution()
    candidates = [2, 3, 5]
    target = 8
    print(cl.combinationSum(candidates, target))