# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # def isPalindrome(self, head: ListNode) -> bool:
    #     # 不可 从新指向头结点 会成环 需要建立新的链表

    #     count = 0
    #     temp = head
    #     while temp:
    #         temp = temp.next
    #         count += 1
    #     if count % 2 == 1:
    #         countfast = count//2 + 1
    #     else:
    #         countfast = count//2
    #     fast = head
    #     stack = []
    #     while countfast != 0:
    #         stack.append(fast.val)
    #         fast = fast.next
    #         countfast -= 1   
    #     if count % 2 == 1:
    #         stack.pop()
    #     while fast and stack:
    #         val = stack.pop()
    #         if val != fast.val:
    #             return False
    #         fast = fast.next
    #     return True
 
    '''
    palindrome list be reversed should equal to origin linklist
    '''
    
    #
    
#     def isPalindrome(self, head: ListNode) -> bool:
#         stack = []
#         pal = head
#         while pal:
#             stack.append(pal.val)
#             pal = pal.next
#         while head:
#             val = stack.pop()
#             if head.val != val: return False
#             head = head.next
#         return True
    
    #

#     def isPalindrome(self, head: ListNode) -> bool:
#         if not head or not head.next: return True
#         stack = [head.val]
#         fast, slow = head, head
#         while fast.next and fast.next.next:
#             fast = fast.next.next
#             slow = slow.next
#             stack.append(slow.val)
#         if not fast.next: stack.pop()
#         while slow.next:
#             val = stack.pop()
#             slow = slow.next
#             if slow.val != val: return False
#         return True

    # not stack O(1) space

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        last = slow.next
        pre = head
        while last.next:
            temp = last.next
            last.next = temp.next
            temp.next = slow.next
            slow.next = temp
        while slow.next:
            slow = slow.next
            if pre.val != slow.val: return False
            pre = pre.next
        return True
