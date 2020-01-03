# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # 1
    
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if not head or not head.next: return head
#         prev = head
#         cur = head.next
#         # NoneType object has no attribute 'next', so should have cur
#         while cur and cur.next:
#             temp = prev.next
#             prev.next = cur.next
#             cur.next = cur.next.next
#             prev.next.next = temp
#             prev = prev.next
#             cur = cur.next
#         return head

    # 2 brilliant 
    
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        odd = head
        even = even_head = head.next
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = even_head
        return head
    