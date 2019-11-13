class Solution:
    def removeDuplicateLetters(self, s):
        m, visited = {}, {}
        res = "0"
        for i in s:
            m[i] = m.get(i, 0) + 1
        for i in s:
            m[i] -= 1
            if i in visited and visited[i] != 0:
                continue
            while res[-1] > i and m[res[-1]] != 0:
                visited[res[-1]] = 0
                res = res[:-1]
            res += i 
            visited[i] = 1
        return res[1:]
if __name__ == "__main__":
    cl = Solution()
    s = 'bcabc'
    print(cl.removeDuplicateLetters(s))