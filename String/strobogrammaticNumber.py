class Solution:
    def isStrobogrammatic(self, s):
        m = { '9': 6, '8': 8, '6': 9, '1': 1, '0': 0}
        i, j = 0, len(s)-1
        while i <= j:
            if m.get(s[i], -1) != int(s[j]):
                return False
            i += 1
            j -= 1
        return True
    
if __name__ == "__main__":
    cl = Solution()
    s = "978"
    print(cl.isStrobogrammatic(s))