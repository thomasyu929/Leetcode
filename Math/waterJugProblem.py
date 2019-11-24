class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:

        '''
        裴蜀定理 ax + by = m
        有整数解时 当且仅当 m 为 a和b 的最大公约数
        '''
        a, b = x, y
        while y:
            d = x % y
            x = y
            y = d
        d = x
        return (z == 0) or (a + b >= z and z % d == 0)    
    
    
        # 2 recursion
        
#         return (z == 0) or (x + y >= z and z % self.gcd(x, y) == 0)

#     def gcd(self, x, y):
#         if y == 0:
#             return x
#         else:
#             self.gcd(y, x % y)

if __name__ == "__main__":
    cl = Solution()
    x = 3
    y = 5
    z = 4
    print(cl.canMeasureWater(x, y, z))