"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    
    # recursive     root.next defaults to #
    
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root: return None
    #     if root.left: root.left.next = root.right
    #     if root.right: root.right.next = root.next.left if root.next else None
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

    # two pointers

    def connect(self, root):
        if not root: return None
        start = root
        while start.left:
            node = start
            while node:
                node.left.next = node.right
                if node.next: node.right.next = node.next.left
                node = node.next
            start = start.left
        return root
            
