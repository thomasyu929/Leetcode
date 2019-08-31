class Solution:
    def findCelebrity(self, n):
        res = 0
        for i in range(n):
            if knows(res, i):
                res = i

        # for i in range(n):
        #     if (res != i and knows(res, i)) or (not knows(i, res)):
        #         return -1
        
        for i in range(res):
            if not knows(i, res) or knows(res, i):
                return -1
        for i in range(res+1, n):
            if not knows(i, res):
                return -1
        return res
