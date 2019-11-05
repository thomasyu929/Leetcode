class Solution:
    def longestCommonPrefix(self, strs):
        
        # 1

        if len(strs) is 0 or len(strs[0]) is 0:
            return ""
        for j in range(len(strs[0])):
            if j >= len(strs[i]) or strs[0][j] != strs[i][j]:
                return strs[0][:j]
        return strs[0]

        # 2 sort solution
        if len(strs) is 0 or len(strs[0]) is 0:
            return ""
        strs.sort()
        lens = min(len(strs[0]), len(strs[-1]))
        for i in range(lens):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]