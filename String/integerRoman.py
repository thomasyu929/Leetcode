class Solution:
    def intToRoman(self, num: int) -> str:
        
        '''
        Every situation like these:
            first   1 ~ 3
        C       100
        CC      200
        CCC     300
            second  4
        CD      400
            third   5 ~ 8
        D       500
        DC      600
        DCC     700
        DCCC    800
            fourth  9
        CM      900
        '''
         
        # 1 brute-force
        
        v1 = ["", "M", "MM", "MMM"]
        v2 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        v3 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        v4 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        res = v1[num//1000] + v2[(num%1000)//100] + v3[((num%1000)%100)//10] + v4[((num%1000)%100)%10]
        return res
    
        # 2
        
        roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        value = [1000, 500, 100, 50, 10, 5, 1]
        
        res = ""
        
        for i in range(0, 7, 2):
            n = num // value[i]
            if n < 4 and n > 0:
                for _ in range(n):
                    res += roman[i] 
            elif n == 4:
                res += roman[i] + roman[i-1]
            elif n > 4 and n < 9:
                res += roman[i-1]
                for _ in range(n-1, 4, -1):
                    res += roman[i]
            elif n == 9:
                res += roman[i] + roman[i-2]
            num %= value[i]
        return res

            
        # 3 Greedy Algorthim
        
        res = ""
        
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        for i in range(len(value)):
            while num >= value[i]:
                num -= value[i]
                res += roman[i]
        return res

if __name__ == "__main__":
    cl = Solution()
    num = 2987
    print(cl.intToRoman(num))