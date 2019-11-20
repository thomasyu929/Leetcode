class Solution:
    def generateParenthesis(self, n):
        res = []
        self.generateParenthesisDFS(n, n, "", res)
        return res
    
    def generateParenthesisDFS(self, left, right, out, res):
        if left > right:
            return
        if left == 0 and right == 0:
            res.append(out)
        else:
            if left > 0:
                self.generateParenthesisDFS(left-1, right, out + '(', res)
            if right > 0:
                self.generateParenthesisDFS(left, right - 1, out + ')', res)

if __name__ == "__main__":
    cl = Solution()
    n = 3
    print(cl.generateParenthesis(n))