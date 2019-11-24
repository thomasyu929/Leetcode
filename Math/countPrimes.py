class Solution:
    
    # 1 brute-force solution    Time Limit Exceeded
    
#     def countPrimes(self, n: int) -> int:
#         if n <= 1:
#             return 0
#         count = 0
#         for i in range(2, n):
#             if self.isPrimes(i) == True:
#                 count += 1
#         return count
        
#     # It can be optimized   n -> n // 2 -> sqrt(n)
#     def isPrimes(self, n):
#         i = 2
#         while i*i <= n:
#             if n % i == 0:
#                 return False
#             i += 1
#         return True

    # 2
    
    # def countPrimes(self, n: int) -> int:
    #     def helper(n, dp):
    #         for i in range(2, n):
    #             if dp[i] == 1:
    #                 k = i * i
    #                 if k >= n:
    #                     return
    #             while k < n:
    #                 dp[k] = 0
    #                 k += i
    #     if n <= 1:
    #         return 0
    #     dp = [1] * n
    #     dp[0], dp[1] = 0, 0
    #     helper(n, dp)

    #     return sum(dp)

    # 3
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5)+1):
            if primes[i] == False:
                continue
                
#           primes[i * i: n: i] = [False] * len(primes[i * i: n: i])

            for j in range(i*i, n, i):
                primes[j] = False
        return sum(primes)

if __name__ == "__main__":
    cl = Solution()
    n = 12
    print(cl.countPrimes(n))