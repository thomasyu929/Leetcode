class Solution:
    def countAndSay(self, n: int) -> str:
        if not n:
            return ""
        res = '1'
        while n > 1:
            cur = ""
            pre = res[0]
            count = 1
            for i in range(1, len(res)):
                if pre == res[i]:
                    count += 1
                else:
                    cur += str(count) + pre
                    pre = res[i]
                    count = 1
            cur += str(count) + pre
            res = cur
            n -= 1
        return res
if __name__ == "__main__":
    cl = Solution()
    n = 5
    print(cl.countAndSay(n))