class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x >= 0:
        #     return x == int(str(x)[::-1])
        # else:
        #     return False
        
        '''
        without convert to string
        '''
        
        if x < 0:
            return False
        p, res = x, 0
        while p:
            res = res * 10 + p % 10
            p //= 10
        return res == x