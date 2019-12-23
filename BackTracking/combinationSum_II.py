class Solution:
    
    # recursive
    
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort()
#         self.helper(candidates, target, 0, [], res)
#         return res
    
#     def helper(self, candidates, target, index, path, res):
#         if target < 0: return 
#         if target == 0: 
#             # if path in res: return
#             # else: return res.append(path)
#             return res.append(path)
#         for i in range(index, len(candidates)):
#             if i > index and candidates[i] == candidates[i-1]: continue
#             self.helper(candidates, target-candidates[i], i+1, path+[candidates[i]], res)
    
    # iteration
    
    def combinationSum2(self, candidates, target):
        candidates.sort()
        dp = [set() for i in range(target+1)]
        dp[0].add(())
        for num in candidates:
            for i in range(target, num-1, -1):
                for a in dp[i-num]:
                    dp[i].add(a + (num,))   # num, be a tuple  and tuple can be set
        return list(dp[-1])

    # didn/t work
    
#     def combinationSum2(self, candidates, target):
#         candidates.sort()
#         dp = []
#         for i in range(1, target+1):
#             cur = set()
#             for num in candidates:
#                 if num > i: break
#                 if num == i: 
#                     cur.add((num,))
#                     break
#                 for t in dp[i-num-1]:
#                     if num >= max(t):
#                         cur.add(t+(num,))
#             dp.append(cur)
#             print(dp)
#             print("\n")
#         return dp[-1]
        
        
    

        
if __name__ == "__main__":
    cl = Solution()
    candidates = [2,5,2,1,2]
    target = 5
    print(cl.combinationSum2(candidates, target))
        
    