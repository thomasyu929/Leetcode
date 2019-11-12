class Solution:
    def convert(self, s, numRows):

        # 1

        from functools import reduce
        from operator import add

        # if numRows == 0 or numRows == 1:
        #     return s
        # zigzag = [[] for i in range(numRows)]
        # row, step = 0, 1
        # for c in s:
        #     zigzag[row] += c
        #     if row == 0:
        #         step = 1
        #     elif row == numRows - 1:
        #         step = -1
        #     row += step
        # return "".join(reduce(add, zigzag))

        # return "".join(["".join(zigzag[i]) for i in range(numRows)])


        # regular

        if numRows == 1 or numRows >= len(s):
            return s
        zigzag = [[] for i in range(numRows)]
        for i in range(len(s)):
            zigzag[numRows-1 - abs(numRows-1 - i % (2*numRows - 2))].append(s[i])
        return "".join(reduce(add, zigzag))

    

if __name__ == "__main__":
    cl = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(cl.convert(s, numRows))