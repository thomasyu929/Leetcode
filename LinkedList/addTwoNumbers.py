# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # linkedlist to str to linkedlist

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        strl1, strl2 = self.strList(l1, ""), self.strList(l2, "")
        suml = int(strl1) + int(strl2)
        print(suml)
        prev = dummy = ListNode(-1)
        for i in reversed(str(suml)):
            prev.next = ListNode(i)
            prev = prev.next
            
        return dummy.next
    
    def strList(self, head, strl):
        while head:
            strl = str(head.val) + strl
            head = head.next
        return strl
    
    # linkedlist one-by-one plus

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            suml = val1 + val2 + carry
            carry = suml // 10
            val = suml % 10
            cur.next = ListNode(val)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry: cur.next = ListNode(1)
        return dummy.next