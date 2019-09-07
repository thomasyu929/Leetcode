class Solution:
    def hIndex(self, citation):
        citations.sort(reverse=True)
        i = 0
        for i in range(len(citation)):
            if i >= citation[i]:
                return i
        return len(citations)