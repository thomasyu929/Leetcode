class Solution:
    def generatePossibleNextMoves(self, s):
        l = list(s)
        p = []
        for i in range(len(l)-1):
            if l[i] == "+" and l[i+1] == "+":
                l[i], l[i+1] = "-", "-"
                p.append("".join(l))
                l = list(s)
        if l[0] == l[len(l)-1] == "+":
            l[0], l[len(l)-1] = "-", "-"
            p.append("".join(l))
        return p

if __name__ == "__main__":
    cl = Solution()
    s = "+++--+-+++-+"
    print(cl.generatePossibleNextMoves(s))