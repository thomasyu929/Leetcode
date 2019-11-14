class Solution:
    def romanToInt(self, s: str) -> int:
        
        # 放在大数的左边只能用一个
        
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if (i == len(s) - 1) or (roman[s[i]] >= roman[s[i+1]]):
                res += roman[s[i]]
            else:
                res -= roman[s[i]]
        return res

if __name__ == "__main__":
    cl = Solution()
    s = "MMCCCXCIX"
    print(cl.romanToInt(s))