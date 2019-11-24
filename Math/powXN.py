class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # 0
        # return x ** n
        
        # 1
        # return pow(x, n)
        
        # 2
        res = 1
        if n == 0:
            return res
        if n < 0:
            n = -n
            x = 1/x
        while n:
            if n % 2 == 1:
            # if n & 1:   
                res *= x
            x *= x
            n //= 2
            # n >>= 1
        return res

if __name__ == "__main__":
    cl = Solution()
    x = 2.00000
    n = 7
    print(cl.myPow(x, n))