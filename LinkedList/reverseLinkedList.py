class Solution:

    # def reverseList(self, head):
    #     prev = None
    #     while head:
    #         curr = head
    #         head = head.next
    #         curr.next = prev
    #         prev = curr
    #     return prev 

    # def reverseList(self, head):
    #     if not head or not head.next:
    #         return head
    #     newHead = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return newHead

    def reverseList(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = prev.next
        while cur and cur.next:
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next