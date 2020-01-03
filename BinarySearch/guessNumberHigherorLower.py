# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    
    # Here "My" means the number which is given for you to guess not the number you put into guess(int num).
    
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right-left)//2
            if guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == -1:
                right = mid
            else:
                return mid
        return right
                