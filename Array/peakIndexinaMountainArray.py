class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        # 1
        
#         return A.index(max(A))
         
        # 2
        
#         for i in range(1, len(A)-1):
#             if A[i] > A[i-1] and A[i] > A[i+1]:
#                 return i
        
        # 3
        
        left, right = 0, len(A)-1
        while left < right:
            mid = left + (right-left)//2
            if A[mid] < A[mid+1]:
                left = mid+1
            else:
                right = mid
        return right