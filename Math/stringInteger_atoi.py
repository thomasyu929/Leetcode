class Solution:
    def myAtoi(self, str: str) -> int:
        s = list(str.lstrip())
        res = []
        for i in range(len(s)):
            if s[i] < '0' or s[i] > '9':
                if i == 0 and (s[i] == '-' or s[i] == '+'):
                    continue
                else:
                    break
            elif s[i] >= '0' and s[i] <= '9':
                res.append(s[i])
        if "".join(res) == "":
            return 0
        res = int("".join(res)) if s[0] != '-' else -int("".join(res))
        return res if res <= 2**31-1 and res >= -2**31 else (2**31-1 if res > 0 else -2**31)

if __name__ == "__main__":
    cl = Solution()
    str = "    .1"
    print(cl.myAtoi(str))