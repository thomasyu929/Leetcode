class Solution:
    def plusOne(self, digits):
        res, final = [], []
        res.extend(str(i) for i in digits)
        res = int("".join(res))
        res += 1
        res = str(res)
        final.extend(int(i) for i in res)
        return final

if __name__ == "__main__":
    cl = Solution()
    digits = [1, 2, 3]
    print(cl.plusOne(digits))