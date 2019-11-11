class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        n = {}
        for i in s:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
                
        for i in t:
            if i in n:
                n[i] += 1
            else:
                n[i] = 1
        return m == n