class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # dict solution
        
        m = {}
        
        for i in s:
            if i in m.keys():
                m[i] += 1
            else:
                m[i] = 1
        for i in range(len(s)):
            if m[s[i]] == 1:
                return i
        return -1
        
        # built-in solution

        c = []
        for i in set(s):
            if s.count(i) == 1:
                c.append(s.index(i))
        if len(c) > 0:  
            return min(c)
        else:
            return -1