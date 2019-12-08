# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    
    # 1 Recursive
    
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         res = [0]
#         self.helper(root, 1, res)
        
#         return res[0]
    
#     def helper(self, root, count, res):
#         if not root.left and not root.right:
#             res[0] = max(res[0], count)
#         if root.left:
#             self.helper(root.left, count+1, res)
#         if root.right:
#             self.helper(root.right, count+1, res)
    
    # 2 queue
    
#     def maxDepth(self, root: TreeNode):
        
#         from collections import deque
        
#         if not root:
#             return 0
#         res = 0
#         queue = deque([(root, 1)])
        
#         while queue:
#             node, count = queue.popleft()
#             if not node.left and not node.right:
#                 res = max(res, count)
#             if node.left:
#                 queue.append((node.left, count+1))
#             if node.right:
#                 queue.append((node.right, count+1))
#         return res