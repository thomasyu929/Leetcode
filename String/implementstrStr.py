class Solution:
    def strStr(self, haystack, needle):
        if len(needle) is 0:
            return 0
        for i in range(len(haystack)+1):
            for j in range(len(needle)+1):
                if j == len(needle):
                    return i 
                if (i+j) == len(haystack):
                    return -1
                if haystack[i+j] != needle[j]:
                    break