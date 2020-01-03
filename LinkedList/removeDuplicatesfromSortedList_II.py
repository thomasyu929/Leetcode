# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # iteration
    
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         dummy = ListNode(-1)
#         dummy.next = head
#         pre = dummy
#         cur = head
#         while cur and cur.next:
#             if cur.next.val == cur.val:
#                 while cur and cur.next and cur.next.val == cur.val:
#                     cur = cur.next
#                 pre.next = cur.next
#                 cur = cur.next
#             else:
#                 pre = pre.next
#                 cur = cur.next
#         return dummy.next
    
    # recursive
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        head.next = self.deleteDuplicates(head.next)
        return head
            
        