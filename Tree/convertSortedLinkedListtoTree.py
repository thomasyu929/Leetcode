# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Stupid Recursion solution
    
    # def sortedListToBST(self, head: ListNode) -> TreeNode:
    #     nums = []
    #     self.helper(head, nums)
    #     return self.arraytoBST(nums)
    
    # def helper(self, head, nums):
    #     if not head: return
    #     nums.append(head.val)
    #     self.helper(head.next, nums)
    
    # def arraytoBST(self, nums):
    #     if not nums: return None
    #     left, right = 0, len(nums)-1
    #     mid = len(nums) // 2
    #     root = TreeNode(nums[mid])
    #     root.left = self.arraytoBST(nums[:mid])
    #     root.right = self.arraytoBST(nums[mid+1:])
    #     return root

    # slow and fast Recursive Solution

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        pre, fast, slow = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        if pre:
            pre.next = None
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root