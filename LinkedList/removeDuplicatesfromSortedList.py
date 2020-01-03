# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # iteration
    # 指向第一个重复的值
    
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         node = head
#         while node and node.next:
#             if node.val == node.next.val:
#                 # temp = node.next
#                 node.next = node.next.next
#                 # temp.next = None
#             else:
#                 node = node.next
#         return head
    
    # recursive
    # 只想最后一个重复的值
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head

    
            
        