# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # stupid solution
    
#     def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#         if m == n: return head
#         mNode = head
#         if m != 1:
#             for _ in range(m-2):
#                 mNode = mNode.next
#             preNode = mNode
#             mNode = mNode.next
#         pre = None
#         end = mNode
#         for _ in range(m, n+1):
#             cur = mNode
#             mNode = mNode.next
#             cur.next = pre
#             pre = cur
#         if m != 1:
#             preNode.next = pre
#             end.next = mNode
#             return head
#         else:
#             end.next = mNode
#             return pre
    
    # iteration dummy
    
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for _ in range(m-1): prev = prev.next
        cur = prev.next
        for _ in range(m, n):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next
        
        
        
    
            
        