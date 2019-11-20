class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # 1 Time Limit Exceeded
        
        # if divisor == 1:
        #     return dividend if dividend <= 2**31-1 else 2**31-1
        # elif divisor == -1:
        #     return -dividend if -dividend <= 2**31-1 else 2**31-1
        
        # count = 0
        # res = 0
        # if dividend < 0 and divisor < 0:
        #     dividend, divisor = -dividend, -divisor
        # if dividend < 0 or divisor < 0:
        #     dividend, divisor = abs(dividend), abs(divisor)
        #     while dividend >= res:
        #         res += divisor
        #         count += 1
        #     return -(count-1)
        # else:
        #     while dividend >= res:
        #         res += divisor
        #         count += 1
        #     return count-1

        # 2

        if dividend == 0:
            return 0

        i, result, p, q = map(abs, (0, 0, dividend, divisor))

        while q << i <= p:
            i += 1

        for j in reversed(range(i)):
            if q << j <= p:
                p = p - (q << j)
                result += 1 << j
        
        if (dividend > 0) != (divisor > 0): 
            result = -result
        return min(result, (1<<31) -1)


if __name__ == "__main__":
    cl = Solution()
    dividend = 17
    divisor = 2
    print(cl.divide(dividend, divisor))