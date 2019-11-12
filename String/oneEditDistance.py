class Solution:
    def isOneEditDistance(self, s, t):

    # only three possiblities

        if len(s) < len(t):
            s, t = t, s
        diff = len(s) - len(t)
        if diff > 1:
            return False
        elif diff == 1:
            for i in range(len(t)):
                if s[i] != t[i]:
                    return s.strip(s[i]) == t
            return True
        else:
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count += 1
            return count == 1
            
if __name__ == "__main__":
    cl = Solution()
    s = 'abc'
    t = 'abc'
    print(cl.isOneEditDistance(s, t))