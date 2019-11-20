class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # 1 built-in 
        
        # return str(int(num1) * int(num2))
    
        # 2 
        nums1, nums2 = [], []
        for i in num1:
            nums1.append(ord(i) - ord('0'))
        for i in num2:
            nums2.append(ord(i) - ord('0'))
        n1, n2 = 0, 0
        x = 1
        for i in range(len(nums1)-1, -1, -1):
            n1 += nums1[i]*x
            x *= 10
        x = 1
        for i in range(len(nums2)-1, -1, -1):
            n2 += nums2[i]*x
            x *= 10
        return str(n1*n2)

if __name__ == "__main__":
    cl = Solution()
    num1 = '0'
    num2 = '3'
    print(cl.multiply(num1, num2))