# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # iteration
    
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode(-1)
#         prev = dummy
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 prev.next = l1
#                 l1 = l1.next
#             else:
#                 prev.next = l2
#                 l2 = l2.next
#             prev = prev.next
#         prev.next = l1 if l1 else l2
        
#         return dummy.next

    # recursive
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            