class Solution:
    # def letterCombinations(self, digits):
    #     if len(digits) == 0:
    #         return []
    #     res = []
    #     m = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
    #     # should use list
    #     self.helper(digits, 0, m, res, "")
    #     return res
    # def helper(self, digits, index, m, res, path):
    #     if len(digits) == len(path):
    #         return res.append(path)
    #     for letter in m[int(digits[index])]:
    #         self.helper(digits, index+1, m, res, path+letter)
        
    def letterCombinations(self, digits):
        if not digits: return []
        res = [""]
        m = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for i in digits:
            temp = []
            for letter in m[int(i)]:
                for s in res:
                    temp.append(s + letter)
            res = temp
        return res

if __name__ == "__main__":
    cl = Solution()
    digits = "23"
    print(cl.letterCombinations(digits))