class Solution:
    def mySqrt(self, x):

        # # 0
        # return int(x**0.5)
        
        # 1 built-in solution
        
        # import math 
        # return int(math.sqrt(x))
        
        # 2  Time Limited Exceeded

        # i = 1
        # while x != i*i:
        #     if x == float(i * i):
        #         break
        #     elif x > float(i * i) and x < float((i+1)*(i+1)):
        #         break
        #     i += 1
        
        # return i

        # 3  Binary search
        
        # if x <= 1:
        #     return x
        # mid = 0
        # left, right = 1, x
        # # while left < right:
        # #     mid = left + (right-left) // 2
        # #     if mid*mid > x:
        # #         right = mid
        # #     else:
        # #         if (mid+1)*(mid+1) > x:
        # #             return mid
        # #         else:
        # #             left = mid + 1
        # # return mid 

        # while left < right:
        #     mid = left + (right - left) // 2
        #     if x / mid >= mid:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return right - 1


        # 4 Newton iteration

        if x == 0:
            return 0
        last = 0
        res = 1
        while last != res:
            last = res
            res = (res + x / res) / 2
        
        return int(last)
        


if __name__ == "__main__":
    cl = Solution()
    x = 8
    print(cl.mySqrt(x))