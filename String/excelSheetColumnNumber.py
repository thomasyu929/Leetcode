class Solution:
    def titleToNumber(self, s: str) -> int:
        n, j = len(s), len(s)-1
        sq = 1
        res = ord(s[-1]) - ord('A') + 1
        if n == 1:
            return res
        for i in range(len(s)-1):
            for _ in range(j):
                sq *= 26 
            res += (ord(s[i]) - ord('A') + 1) * sq
            sq = 1
            j -= 1
        return res

    # neat solution

    def titleToNumber(self, s: str) -> int:
        n = len(s)
        sq = 1
        res = 0
        for i in range(len(s)-1, -1, -1):
            res += (ord(s[i]) - ord('A') + 1) * sq
            sq *= 26
        return res
if __name__ == "__main__":
    cl = Solution()
    s = "ABCD"
    print(cl.titleToNumber(s))