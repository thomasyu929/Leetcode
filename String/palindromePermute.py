class Solution:
    def canPermutePalindrome(self, s):
        m = {}
        count = 0
        for i in s:
            m[i] = m.get(i, 0) + 1
        for i in s:
            if m[i] % 2 == 0:
                continue
            if m[i] % 2 == 1:
                count += 1
            if count > 1:
                return False
        return True

if __name__ == "__main__":
    cl = Solution()
    s = 'bbaccddd'
    print(cl.canPermutePalindrome(s))