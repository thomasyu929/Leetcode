# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        # Recursion
        
        # if not nums: return None
        # left, right = 0, len(nums)-1
        # mid = len(nums) // 2
        # node = TreeNode(nums[mid])
        # node.left = self.sortedArrayToBST(nums[:mid])
        # node.right = self.sortedArrayToBST(nums[mid+1:])
        
        # return node
    
        if not nums: return None
        root = TreeNode(0)
        stack = [(root, 0, len(nums)-1)]
        while stack:
            node, left, right = stack.pop()
            mid = (left + right) // 2
            node.val = nums[mid]
            if left <= mid - 1:
                node.left = TreeNode(0)
                stack.append((ndoe.left, left, mid - 1))
            if mid + 1 <= right:
                node.right = TreeNode(0)
                stack.append((node.right, mid + 1, right))
        return root