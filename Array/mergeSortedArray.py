class Solution:
    def merge(self, nums1, nums2):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(m, len(nums1)):
        #     nums1.pop(m)
        # for i in nums2:
        #     nums1.append(i)
        # nums1.sort()
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
