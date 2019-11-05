class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # oneline solution
        return len(s.rstrip(' ').split(' ')[-1])

        # normal solution
        
        count = 0
        if len(s) is 0:
            return 0
        for i in range(len(s)-1, -1, -1):
            if s[i] is not " ":
                count += 1
                if s[i-1] is " ":
                    break
        return count