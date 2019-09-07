class Solution:
    def shortDistance(words, word1, word2):
        # p1, p2 = len(words), -len(words)
        # for i in range(len(words)):
        #     if words[i] == word1:
        #         if word1 == word2:
        #             p1 = p2
        #         else:
        #             p1 = i 
        #     if words[i] == word2:
        #         p2 = i
        #     minDtn = min(minDtn, abs(p1-p2))

        idx = -1 
        for i in range(len(words)):
            if words[i] == word1 or words[i] == word2:
                if idx != -1 and (word1 == word2 or words[i] != words[idx]):
                    minDtn = min(minDtn, i - idx)
                idx = i

    return minDtn                
