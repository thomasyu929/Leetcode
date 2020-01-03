# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        
        '''
        1. find the midpiont, break, make it to be two LinkedLists
        2. reverse second LinkedList
        3. insert second to first
        '''
        # if not head or not head.next: return
        # fast, slow = head, head
        # while fast.next and fast.next.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # l1 = head
        # l2 = slow.next
        # slow.next = None
        # prev = None
        # while l2:
        #     cur = l2
        #     l2 = l2.next
        #     cur.next = prev
        #     prev = cur
        # l2 = prev
        # while l2:
        #     temp = l1.next
        #     l1.next = l2
        #     l2 = l2.next
        #     l1.next.next = temp
        #     l1 = temp
        
        # use stack
        
        if not head or not head.next: return 
        c = head
        stack = []
        while c:
            stack.append(c)
            c = c.next
        l = len(stack)
        count = (l-1) // 2
        cur = head
        while count:
            node = stack.pop()
            temp = cur.next
            cur.next = node
            node.next = temp
            cur = temp
            count -= 1
        stack[-1].next = None

if __name__ == "__main__":
    cl = Solution()
    head = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    head.next = n2
    n2.next = n3
    n3.next = n4
    print(cl.reorderList(head))