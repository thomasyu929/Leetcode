class Solution:
    # def getFactors(self, n):
    #     res = []
    #     self.helper(n, 2, [], res)
    #     return res
    # def helper(self, n, index, out, res):
    #     if n == 1 and len(out) > 1:
    #         res.append(out)
    #     for i in range(index, n+1):
    #         if n % i == 0:
    #             self.helper(n//i, i, out+[i], res)

    #

    def getFactors(self, n):
        from math import sqrt

        res, out = [], []
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                v = self.getFactors(n//i)
                res += [[i, n//i]]
                for a in v:
                    if i <= a[0]:
                        a = [i] + a
                        res += [a]
        return res




if __name__ == "__main__":
    cl = Solution()
    n = 12
    print(cl.getFactors(n))