class Solution:
    
    # built-in function
    
    # def combine(self, n, k):
    
    #     from itertools import combinations
    
    #     return list(combinations(range(1, n+1), k))
    
    # slow solution
    
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     res = [[]]
    #     ans = []
    #     nums = list(range(1, n+1))
    #     for num in nums:
    #         path = []
    #         for i in res:
    #             s = i + [num]
    #             path.append(s)
    #             if len(s) == k:
    #                 ans.append(s)
    #         res += path
    #     return ans
    
    # recursive solution
    
#     def combine(self, n, k):
#         res = []
#         self.helper(1, [], n, k, res)
#         return res
    
#     def helper(self, index, out, n, k, res):
#         if len(out) == k: return res.append(out) 
#         for i in range(index, n+1):
#             self.helper(i+1, out+[i], n, k, res)
            
    # recursive use defination C(n, k) = C(n-1, k-1) + C(n-1, k)     
    
    # def combine(self, n, k):
    #     if k == 1: return [[i] for i in range(1, n+1)]
    #     elif k == n: return [list(range(1, n+1))]
    #     else:
    #         res = []
    #         res += self.combine(n-1, k)
    #         path = self.combine(n-1, k-1)
    #         for i in path:
    #             i.append(n)
    #         res += path
    #         return res
    
    # iteration
    
#     def combine(self, n, k):
#         res = []
#         out = [0]*k
#         i = 0
#         while i >= 0:
#             out[i] += 1
#             if out[i] > n: i -= 1
#             elif i == k-1: res.append(out[:])
#             else:
#                 i += 1
#                 out[i] = out[i-1]
                
#         return res
         