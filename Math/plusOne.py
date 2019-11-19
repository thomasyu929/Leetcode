class Solution:
    
    # # 1 
    
    # def plusOne(self, digits):
    #     res = []
    #     res.extend(str(i) for i in digits)
    #     return [int(i) for i in str(int("".join(res)) + 1)]
    
    # # similar as this:
    
    # def plusOne(self, digits):
    #     return [int(i) for i in str(int("".join(map(str, digits))) + 1)]
    
    # 2
    
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        if digits[0] == 0:
            digits = [1] + digits
        return digits
        

if __name__ == "__main__":
    cl = Solution()
    digits = [8, 9, 9]
    print(cl.plusOne(digits))