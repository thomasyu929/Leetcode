class Solution:
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
    
    
    '''
    初始化两个长度为256的数组，因为ASCII码只有256字符
    i+1 是 确保在对应索引位置加一
    '''
    def isIsomorphic(self, s, t):
        d1, d2 = [0]*256, [0]*256
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i+1
            d2[ord(t[i])] = i+1
        return True