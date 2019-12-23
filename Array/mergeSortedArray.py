class Solution:
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        nums1 = nums[:len(nums)//2]
        nums2 = nums[len(nums)//2:]
        nums1 = self.mergeSort(nums1)
        nums2 = self.mergeSort(nums2)

        return self.merge(nums1, nums2)

    def merge(self, nums1, nums2):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        while j >= 0:
            nums1[k] > nums2[j]
            k -= 1
            j -= 1


