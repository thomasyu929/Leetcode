class Solution:

    '''
    同一组的词 letter之间与首字母有相同的偏移量
    '''

    def groupStrings(self, strings):
        m = {}
        res = []
        for s in strings:
            ha = []
            for i in range(1, len(s)):
                ha.append(str((ord(s[i]) + 26 - ord(s[0])) % 26))
            h = ','.join(ha)
            m[h] = m.get(h, []) + [s]
        for key in m:
            res.append(m[key])
        return res
if __name__ == "__main__":
    cl = Solution()
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(cl.groupStrings(strings))