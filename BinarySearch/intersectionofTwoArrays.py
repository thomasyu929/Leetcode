class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # 1
        
#         nums1 = list(set(nums1))
#         res = []
#         for i in range(len(nums1)):
#             if nums1[i] in nums2:
#                 res.append(nums1[i])
#         return res

        # 2
    
        return list(set(nums1) & set(nums2))
    
    
