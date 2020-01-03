# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # normal solution
    
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if not headA or not headB: return None
#         countA, countB = self.getLength(headA, 1), self.getLength(headB, 1)
#         if countA > countB:
#             for _ in range(countA - countB):
#                 headA = headA.next
#         elif countA < countB:
#             for _ in range(countB - countA):
#                 headB = headB.next
#         while headA and headB and headA != headB:
#             headA = headA.next
#             headB = headB.next
#         return headA if headA and headB else None
            
#     def getLength(self, head, count):
#         while head: 
#             count += 1
#             head = head.next
#         return count
    
    # brilliant solution
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
            
            
        