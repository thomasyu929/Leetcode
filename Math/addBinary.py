class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res = ""
        x = len(a) - len(b)
        if x > 0:
            b = x*'0' + b
        else:
            a = (-x)*'0' + a
            
        '''
        carry is an important way to as a tag to record and needs to be lenarned        '''
            
        carry = 0
        
        
        for i in range(len(a)-1, -1, -1):    
            n = int(a[i]) + int(b[i])
            if n == 2:
                if carry == 1:
                    res = "1" + res
                else:
                    res = "0" + res
                carry = 1
            elif n == 1:
                if carry == 1:
                    res = "0" + res
                else:
                    res = "1" + res
            elif n == 0:
                res = str(carry) + res
                carry = 0
        if carry == 1:
            res = '1' + res
        return res 

if __name__ == "__main__":
    cl = Solution()
    a = '11'
    b = '1'
    print(cl.addBinary(a, b))