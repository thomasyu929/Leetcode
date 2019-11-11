class Solution:
    def wordPattern(self, pattern, s) -> bool:
#         # 1
        
#         str = str.split()
#         return list(map(str.index, str)) == list(map(pattern.find, pattern))
    
#         # 2
        
#         str = str.split()
#         a = zip(pattern, str)
#         return len(str) == len(pattern) and len(set(a)) == len(set(str)) == len(set(pattern))
        
        # 3
        m = {}
        n = {}
        s = s.split()
        for i in s:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i in pattern:
            if i in n:
                n[i] += 1
            else:
                n[i] = 1
        print(list(i for i in m.values()))
        return [i for i in m.values()] == [i for i in n.values()]
if __name__ == "__main__":
    cl = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(cl.wordPattern(pattern, s))