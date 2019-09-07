class Solution:
    def hIndex(self, citation):
        i = 0
        citations.sort(reverse=True)
        for i in range(len(citation)):
            if i >= citation[i]:
                return i
        return len(citations)