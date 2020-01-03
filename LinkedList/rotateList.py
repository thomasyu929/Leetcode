# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        use fast and slow pointer
        '''
        if not head or not head.next: return head
        c = head
        count = 0
        while c:
            c = c.next
            count += 1
        k %= count
        if k == 0:
            return head
        fast, slow = head, head
        while k > 1:
            fast = fast.next
            k -= 1
        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next
        prev.next = None
        fast.next = head
        return slow
        
        