class Solution:
    # def convertToTitle(self, n: int) -> str:
    #     res = ""
    #     while n > 0:
    #         r = n % 26
    #         if r == 0:
    #             char = "Z"
    #             res += char
    #             n -= 1
    #         else:
    #             char = chr(r + ord('A') - 1)
    #             res += char
    #         n = n // 26
    #     return res[::-1]

    # 2 recrusive
    
    def convertToTitle(self, n: int) -> str:
        return "" if n == 0 else self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))
    # # 3
    
    # def convertToTitle(self, n: int) -> str:
    #     res = ""
    #     while n > 0:
    #         n = n-1
    #         res += chr(n % 26 + ord('A'))
    #         n //= 26
    #     return res[::-1]

if __name__ == "__main__":
    cl = Solution()
    n = 54
    print(cl.convertToTitle(n))
    


