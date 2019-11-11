class Solution:

    # 1

    # def groupAnagrams(self, strs):
    #     d = {}
    #     for i in strs:
    #         key = ''.join(sorted(i))
    #         if key in d:
    #             d.get(key).append(i)
    #         else:
    #             d[key] = [i]
    #     return list(d.values())

    # 2

    '''
    tuple can as hash key
    '''

    # def groupAnagrams(self, strs):
    #     import collections
    #     hmap = collections.defaultdict(list)
    #     for st in strs:
    #         array = [0] * 26
    #         for l in st:
    #             array[ord(l) - ord('a')] += 1
    #         hmap[tuple(array)].append(st)
    #     return list(hmap.values())

    # 3
    
    def groupAnagrams(self, strs):
        import collections
        anagrams = collections.defaultdict(list)
        for string in strs:
            anagrams[tuple(sorted(string))].append(string)
        return list(anagrams.values())

if __name__ == "__main__":
    cl = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(cl.groupAnagrams(strs))