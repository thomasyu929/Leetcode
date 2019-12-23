class Solution:
    
    # recursive
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # nums = list(range(1, 10))
        res = []
        self.helper(n, k, 1, [], res)
        return res
    
    def helper(self, n, k, index, path, res):
        if n < 0: return 
        if len(path) == k and n == 0:
            res.append(path)
            return 
        for i in range(index, 10):
            self.helper(n-i, k, i+1, path+[i], res)
        