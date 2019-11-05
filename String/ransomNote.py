class Solution:
    def canConstruct(self, ransomNote, magazine):
        m = {}
        for i in magazine:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i in ransomNote:
            if i in m:
                m[i] -= 1
                if m[i] < 0:
                    return False
            else:
                return False
        return True