class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n > 0:
          r = n % 26
          if r == 0:
              char = "Z"
              res += char
              n -= 1
          else:
              char = chr(r + ord('A') - 1)
              res += char
          n = n // 26
        return res[::-1]

if __name__ == "__main__":
    cl = Solution()
    n = 28
    print(cl.convertToTitle(n))
    


