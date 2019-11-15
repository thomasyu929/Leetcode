class Solution:

    def isPalindrome(self, s: str) -> bool:
    	s = [i for i in s.lower() if i.isalnum()]
    	return s == s[::-1]
        
    # 2 O(1) space

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s)-1
        while i <= j:
            # if not((s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= '0' and s[i] <= '9') or (s[i] >= 'a' and s[i] <= 'z')):
            
            # can use buile-in function str.isalnum()
            # if not s[i].isalnum():
            
            if self.isAlphaNum(s[i]):
                i += 1
                continue
            
            # if not((s[j] >= 'A' and s[j] <= 'Z') or (s[j] >= '0' and s[j] <= '9') or (s[j] >= 'a' and s[j] <= 'z')):
            if self.isAlphaNum(s[j]):
                j -= 1
                continue

            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    
    def isAlphaNum(self, s):
        return not ((s >= 'A' and s <= 'Z') or (s >= '0' and s <= '9') or (s >= 'a' and s <= 'z'))


if __name__ == "__main__":
    cl = Solution()
    s = "race a car"
    print(cl.isPalindrome(s))