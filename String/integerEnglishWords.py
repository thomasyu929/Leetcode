class Solution:

    # 1 stupid solution

    # def numberToWords(self, num: int) -> str:
    #     if num == 0:
    #         return "Zero"
    #     res = ""
    #     s = str(num)
    #     if len(s) > 9:
    #         res += self.convert(int(s[:len(s)-9])) + " " + "Billion"
    #         if int(s[len(s)-9:len(s)-6]) != 0:
    #             res += " " + self.convert(int(s[len(s)-9:len(s)-6])) + " "+ "Million"
    #         if int(s[len(s)-6:len(s)-3]) != 0:
    #             res += " " + self.convert(int(s[len(s)-6:len(s)-3])) + " " +  "Thousand"
    #         if int(s[len(s)-3:]) != 0:
    #             res += " " + self.convert(int(s[len(s)-3:]))
    #     elif len(s) > 6:
    #         res += self.convert(int(s[:len(s)-6])) + " " + "Million"
    #         if int(s[len(s)-6:len(s)-3]) != 0:
    #             res += " " + self.convert(int(s[len(s)-6:len(s)-3])) + " " +  "Thousand"
    #         if int(s[len(s)-3:]) != 0:
    #             res += " " + self.convert(int(s[len(s)-3:]))
    #     elif len(s) > 3:
    #         res += self.convert(int(s[:len(s)-3])) + " " +  "Thousand"
    #         if int(s[len(s)-3:]) != 0:
    #             res += " " + self.convert(int(s[len(s)-3:]))
    #     else:
    #         res += self.convert(num)
    #     return res
    
    # def convert(self, num):
        
    #     res = ""
        
    #     key1 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"] 
    #     key2 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
    #     if len(str(num)) == 3:
    #         n = num // 100
    #         res += key2[n] + " " + "Hundred"
    #         if int(str(num)[1:]) != 0:
    #             res += " "
    #         num %= 100
    #     if len(str(num)) == 2 and num >= 20:
    #         n = num // 10
    #         res += key1[n]
    #         if num % 10 != 0:
    #             res += " " + key2[num%10]
    #     elif num < 20:
    #         res += key2[num]
    #     return res

    # 2 

    key1 = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"] 
    key2 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    key3 = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        res = ""
        i = 0
        while num > 0:
            if (num % 1000) != 0:
                res = self.convert(num%1000) + key3[i] + " " + res
            num //= 1000
            i += 1
        return res.rstrip()

    def convert(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return key2[num] + " "
        elif num < 100:
            return key1[num//10] + " " + self.convert(num%10)
        else:
            return key2[num//100] + " " + "Hundred" + " " + self.convert(num%100)
        

if __name__ == "__main__":
    cl = Solution()
    num = 10000010
    print(cl.numberToWords(num))