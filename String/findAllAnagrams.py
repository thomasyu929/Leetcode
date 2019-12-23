class Solution:
    
    # time limit exceeded
    
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     # from collections import defaultdict
    #     # m = defaultdict(list)
    #     res = []
    #     p = "".join(sorted(p))
    #     l = len(p)
    #     for i in range(len(s)-l+1):
    #         a = "".join(sorted(s[i:i+l]))
    #         if a == p: res.append(i)
    #     return res
    
    # hashmap
    
    # def findAnagrams(self, s, p):
    #     if len(p) > len(s):
    #         return []
    #     m1, m2, res = [0]*26, [0]*26, []
    #     for i in range(len(p)):
    #         m1[ord(p[i]) - ord('a')] += 1
    #         m2[ord(s[i]) - ord('a')] += 1
    #     if m1 == m2: res.append(0)
    #     for i in range(len(p), len(s)):
    #         m2[ord(s[i]) - ord('a')] += 1
    #         m2[ord(s[i-len(p)]) - ord('a')] -= 1
    #         if m1 == m2: res.append(i-len(p)+1)
    #     return res

    # slide window

    def findAnagrams(self, s, p):

        from collections import Counter

        res = []
        pCount, sCount = Counter(p), Counter(s[:len(p)])
        if pCount == sCount: res.append(0)
        for i in range(len(p), len(s)):
            sCount[s[i]] += 1
            sCount[s[i-len(p)]] -= 1
            if sCount[s[i-len(p)]] == 0:
                del sCount[s[i-len(p)]]
            if sCount == pCount: res.append(i-len(p)+1)
        return res


            
        