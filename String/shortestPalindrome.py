class Solution:

    # 1 brute-force

    # def shortestPalindrome(self, s):
    #     t = s[::-1]
    #     for i in range(len(s)):
    #         if s[:len(s)-i] == t[i:]:
    #             break
    #     return t[:i] + s

    # 2 recrusive

    def shortestPalindrome(self, s):
        i = 0
        if s == s[::-1]:
            return s
        for j in range(len(s)-1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == len(s):
            return s
        return s[i:][::-1] + self.shortestPalindrome(s[:i]) + s[i:]

if __name__ == "__main__":
    cl = Solution()
    s = 'dssda'
    print(cl.shortestPalindrome(s))
