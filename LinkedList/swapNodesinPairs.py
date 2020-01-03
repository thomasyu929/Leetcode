# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # iteration
    
#     def swapPairs(self, head: ListNode) -> ListNode:
#         dummy = ListNode(-1)
#         dummy.next = head
#         pre = dummy
#         while pre.next and pre.next.next:
#             temp = pre.next.next
#             pre.next.next = temp.next
#             temp.next = pre.next
#             pre.next = temp
#             pre = pre.next.next
#         return dummy.next
    
    # recursive
    
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        temp = head.next
        head.next = self.swapPairs(head.next.next)
        temp.next = head
        return temp
            