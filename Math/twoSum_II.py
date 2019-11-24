class Solution:
    
    # 1 same solution as Two Sum
    
    def twoSum(self, numbers, target):
        m = {}
        for i, n in enumerate(numbers):
            x = target - n
            if x in m:
                return m[x]+1, i+1
            else:
                m[n] = i
                
    # 2 
    
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers)-1
        while left <= right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left+1, right+1
        return left+1, right+1

if __name__ == "__main__":
    cl = Solution()
    numbers = [2,7,11,15]
    target = 9
    print(cl.twoSum(numbers, target))