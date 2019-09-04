class Solution:
    def getHint(self, secret, guess):
        from collections import Counter
        c = Counter(secret)
        d = {}
        for i in guess:
            d[i] = 0
        bull = 0
        cow = 0
        for i in range(len(secret)):
            if secret[i] = guess[i]:
                bull += 1
                d[guess[i]] += 1
                if d[guess[i]] > c[guess[i]]:
                    d[guess[i]] = c[guess[i]]
                    cow -= 1
                continue
            elif guess[i] in secret:
                if d[guess[i]] < c[guess[i]]:
                    cow += 1
                    d[guess[i]] += 1
        c = str(bull) + "A" + str(cow) + "B"
        return c