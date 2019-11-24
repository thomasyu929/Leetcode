class Solution:

    # 1 Time Limit Exceeded

    # def threeSum(self, nums):
    #     res = []
    #     for i in range(len(nums)):
    #         m = {}
    #         target = 0 - nums[i]
    #         for j in range(i+1, len(nums)):
    #             x = target - nums[j]
    #             if x in m:
    #                 res.append([nums[i], x, nums[j]])
    #             else:
    #                 m[nums[j]] = j
    #     for i in range(len(res)):
    #         res[i].sort()
    #     ans = []
    #     for i in res:
    #         if i not in ans:
    #             ans.append(i)
        
    #     return ans

    # 2 

    def threeSum(self, nums): 
        res = []  
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    res.append([nums[left], nums[i], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res



if __name__ == "__main__":
    cl = Solution()
    nums = [0,0,0,0,0,0,0,0,0]
    print(cl.threeSum(nums))