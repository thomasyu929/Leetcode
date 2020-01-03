# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(None)
        pre = dummy 
        dummy.next = head
        while pre.next and pre.next.val < x:
            pre = pre.next
        cur = pre
        while cur.next:
            if cur.next.val < x:
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
                pre = pre.next
            else:
                cur = cur.next
        return dummy.next
        
                
                
                
        
        