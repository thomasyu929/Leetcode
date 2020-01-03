class Solution:

    # 1 time limit exceeded

#     def countSmaller(self, nums):
#         res = []
#         for i in range(len(nums)):
#             target = nums[i]
#             record = nums[i+1:]
#             record.sort()
#             left, right = 0, len(record)
#             while left < right:
#                 mid = left + (right-left)//2
#                 if record[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid
#             res.append(right)
#         return res
        
    # 2 
    
    def countSmaller(self, nums):
        res = []
        temp = []
        for i in range(len(nums)-1, -1, -1):
            target = nums[i]
            left, right = 0, len(temp)
            while left < right:
                mid = left + (right-left)//2
                if temp[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            res.append(right)
            temp.insert(right, nums[i])
        return res[::-1]
if __name__ == "__main__":
    cl = Solution()
    nums = []
    print(cl.countSmaller(nums))