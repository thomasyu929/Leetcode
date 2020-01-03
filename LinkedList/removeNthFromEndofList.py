# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # 1
    
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     if head.next == None:
    #         return None
    #     fast = head
    #     for _ in range(n-1):
    #         fast = fast.next
    #     slow = head
    #     pre = head
    #     while fast.next:
    #         fast = fast.next
    #         pre = slow
    #         slow = slow.next
    #     if n == 1:
    #         pre.next = None
    #     else:
    #         slow.val = slow.next.val
    #         slow.next = slow.next.next
    #     return head
    
    # 2
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n): 
            fast = fast.next
        if fast == None: return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        