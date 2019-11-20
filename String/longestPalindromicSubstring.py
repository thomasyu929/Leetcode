class Solution:

    # 1 O(n*n)

    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        start, maxL = 0, 0
        for i in range(len(s)):
            if len(s)-i <= maxL // 2:
                break
            
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if maxL < right - left - 1:
                maxL = right - left - 1
                start = left + 1

            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if maxL < right - left - 1:
                maxL = right - left - 1
                start = left + 1 
        
        return s[start:start+maxL]

    # 2 O(n*n)  don't need check odd and even

    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        start, maxL, i = 0, 0, 0
        while i < len(s):
            if len(s)-i <= maxL // 2:
                break
            
            left, right = i, i
            while right < len(s)-1 and s[right] == s[right+1]:
                right += 1
            i = right + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if maxL < right - left - 1:
                maxL = right - left - 1
                start = left + 1 
        
        return s[start:start+maxL]
        

if __name__ == "__main__":
    cl = Solution()
    s = 'xnoony'
    print(cl.longestPalindrome(s))