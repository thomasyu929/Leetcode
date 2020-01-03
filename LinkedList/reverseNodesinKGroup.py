# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or not head or not head.next: return head
        c = head
        count = 0
        while c:
            c = c.next
            count += 1
        dummy = ListNode(None)
        dummy.next = head
        prev, cur = dummy, head
        while count >= k:
            cur = prev.next
            for _ in range(k-1):
                temp = cur.next
                cur.next = temp.next
                temp.next = prev.next
                prev.next = temp
            prev = cur
            count -= k
        return dummy.next


if __name__ == "__main__":
    cl = Solution()
    head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n4 = ListNode(5)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    k = 2
    print(cl.reverseKGroup(head, k))