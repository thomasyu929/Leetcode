class Solution:
    def reverseWords(self, s):
        word = ""
        words = ""
        s = s[::-1]
        for i, j in enumerate(s):
            if word != "" and j != " " and s[i-1] == " ":
                words += (word + " ")
                word = j
            elif j != " ":
                word = j + word 
            else:
                continue
        words += word

        return list(words)

if __name__ == "__main__":
    sol = Solution()
    
    s= ['this', 'is', 'beauty']
    print (sol.reverseWords(s))
