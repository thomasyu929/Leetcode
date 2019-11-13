class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "/" + s
        return res
    
    def decode(self, strs):
        res = []
        start, end = 0, 0
        while end < len(strs):
            if strs[end] != '/':
                end += 1
            else:
                l = int(strs[start:end])
                res.append([strs[end+1:end+l+1]])
                end += l + 1
                start = end
        return res


if __name__ == "__main__":
    cl = Solution()
    strs = ['abc', 'def435', 'fh']
    print(cl.encode(strs))
    print(cl.decode(cl.encode(strs)))
   