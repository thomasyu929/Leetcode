class Solution:
    def __init__(self, words):
        self.map = {}
        for i in range(len(words)):
            if words[i] in self.map:
                self.map[words[i]].append(i)
            else:
                self.map[word[i]] = [i]
    
    def shortest(self, word1, word2):
        w1 = self.map[word1]
        w2 = self.map[word2]
        for i in range(len(w1)):
            for j in range(len(w2)):
                minDtn = min(minDtn, abs(w1[i] - w2[j]))
        return minDtn