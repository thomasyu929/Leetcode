class Solution:
    def wordDistance(words, word1, word2):
        if words == None or word1 == None or word2 == None:
            return -1
        i, w1, w2 = 0, 0, 0
        for i in range(len(words)):
            if words[i] == word1:
                w1 = i
            elif words[i] == word2:
                w2 = i
            # if w1 - w2 > 0:
            #     return w1 - w2
            # else:
            #     return w2 - w1
            minDtn = abs(w1 - w2)

