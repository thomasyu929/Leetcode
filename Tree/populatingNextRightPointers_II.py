"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Initially, all next pointers are set to NULL.

class Solution:
    
    # recursive     root.next defaults to #
    
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root: return None
    #     node = root.next
    #     while node:
    #         if node.left:
    #             node = node.left
    #             break
    #         if node.right:
    #             node = node.right
    #             break
    #         node = node.next
    #     if root.right: root.right.next = node
    #     if root.left: root.left.next = root.right if root.right else node
    #     self.connect(root.left)
    #     self.connect(root.right)
    #     return root
    
    # iteration
    
    # def connect(self, root):

    #     from collections import deque

    #     if not root: return None
    #     queue = deque([root])
    #     while queue:
    #         l = len(queue)
    #         for i in range(l):
    #             node = queue.popleft()
    #             if node.left: queue.append(node.left)
    #             if node.right: queue.append(node.right)
    #             if i < l-1: node.next = queue[0]
    #     return root

    # constant space
    
    def connect(self, root):
        dummy = Node(0)
        cur = dummy
        head = root
        while root:
            if root.left:
                cur.next = root.left
                cur = cur.next
            if root.right:
                cur.next = root.right
                cur = cur.next
            root = root.next
            if not root:
                cur = dummy
                root = dummy.next
                dummy.next = None
        return head
            