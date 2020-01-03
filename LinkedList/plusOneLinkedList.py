# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # iteration

    # def plusOne(self, head):
    #     plus = True
    #     record = head = self.reverseList(head) 
    #     # while head:
    #     #     if head.val == 9 and plus:
    #     #         head.val = 0 
    #     #         if head.next == None:
    #     #             head.next = ListNode(1)
    #     #             break
    #     #     else:
    #     #         head.val += 1
    #     #         break
    #     #     head = head.next
    #     carry = 1
    #     while head:
    #         prev = head
    #         temp = head.val + carry
    #         head.val = temp % 10
    #         carry = temp // 10
    #         if carry == 0: break
    #         head = head.next
    #     if carry: prev.next = ListNode(1)
    #     return self.reverseList(record)

    # def reverseList(self, head):
    #     prev = None
    #     while head:
    #         cur = head
    #         head = head.next
    #         cur.next = prev
    #         prev = cur
    #     return prev

    # recursive

    def plusOne(self, head):
        if not head: return head
        carry = self.helper(head)
        if carry == 1:
            res = ListNode(1)
            res.next = head
            return res
        return head
    def helper(self, head):
        if not head: return 1
        carry = self.helper(head.next)
        s = head.val + carry
        head.val = s % 10
        return s // 10

if __name__ == "__main__":
    cl = Solution()
    head = ListNode(1)
    n2 = ListNode(5)
    n3 = ListNode(9)
    head.next = n2
    n2.next = n3
    print(cl.plusOne(head))


