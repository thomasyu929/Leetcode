# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

'''
2(a + b + (b+c)n1) = a + b + (b+c)n2
a + b = (b+c)(n2-n1)
m = n2-n1
a = (b+c)(m-1) + c
'''

    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: 
                break
        if not fast or not fast.next:
            return None
        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast