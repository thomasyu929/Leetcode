# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        # 1 dummy
        
#         dummy = ListNode(-1)
#         dummy.next = head
#         prev = dummy
#         # cur = prev.next
#         # while cur:
#         #     if cur.val == val:
#         #         prev.next = cur.next
#         #         cur.next = None
#         #         cur = prev.next
#         #     else:
#         #         prev = cur
#         #         cur = cur.next
#         # return dummy.next
#         while prev.next:
#             if prev.next.val == val:
#                 temp = prev.next
#                 prev.next = temp.next
#                 temp.next = None
#             else:
#                 prev = prev.next
#         return dummy.next

        # 2
#         if not head: return None
#         cur = head
#         while cur.next:
#             if cur.next.val == val:
#                 cur.next = cur.next.next
#             else:
#                 cur = cur.next
        
#         return head.next if head.val == val else head
        
    
        # 3 recursive
        if not head: return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
    
    
        
        