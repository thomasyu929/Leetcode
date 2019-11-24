class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 1:
            return True
        mid = 0 
        left, right = 1, num // 2
        while left <= right:
            mid = (right + left + 1) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
    
if __name__ == "__main__":
    cl = Solution()
    num = 3
    print(cl.isPerfectSquare(num))