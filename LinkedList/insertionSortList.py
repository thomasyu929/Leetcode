# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # need remember

    def insertionSortList(self, head: ListNode) -> ListNode:
        p = dummy = ListNode(-1)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val: 
                cur = cur.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            temp = cur.next
            cur.next = temp.next
            temp.next = p.next
            p.next = temp
        return dummy.next
            
                
                
            