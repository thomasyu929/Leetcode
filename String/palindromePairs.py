class Solution:
    
    # each of word is unique
    
    def palindromePairs(self, words):
        res = []
        m = {}
        for i, word in enumerate(words):
            m[word] = i

        for i, word in enumerate(words):
            if word == "":
                res.extend([(i, j) for j in range(len(words)) if i != j and words[j] == words[j][::-1]])
                continue
            for j in range(len(word)):
                left = word[:j]
                right = word[j:]
                if right == right[::-1] and left[::-1] in m and m[left[::-1]] != i:
                    res.append((i, m[left[::-1]]))
                if left == left[::-1] and right[::-1] in m and m[right[::-1]] != i:
                    res.append((m[right[::-1]], i))
        return res

if __name__ == "__main__":
    
    cl = Solution()
    words = ["abcd","dcba","lls","s","sssll"]
    print(cl.palindromePairs(words))
