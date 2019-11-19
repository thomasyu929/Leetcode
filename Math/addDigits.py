class Solution:
    
    '''
    digital root
    '''
    
    # 1 not good solution
    
    # def addDigits(self, num: int) -> int:
    #     while num // 10 > 0:
    #         res = 0
    #         for i in str(num):
    #             res += int(i)
    #         num = res
    #     return num
    
    # 2 use regular 
    
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        
        # 1 + (num-1) % 9 is a good way to solve some problem
        
        return 1 + (num-1) % 9

if __name__ == "__main__":
    cl = Solution()
    num = 98
    print(cl.addDigits(num))