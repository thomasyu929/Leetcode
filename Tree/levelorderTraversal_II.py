# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Recursive
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.helper(root, 0, res)
        return res[::-1]
    def helper(self, root, level, res):
        if not root:
            return 
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        if root.left: self.helper(root.left, level+1, res)
        if root.right: self.helper(root.right, level+1, res) 
        
    # Iteration
    
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
#         from collections import deque
        
#         if not root:
#             return []
#         queue = deque([root])
#         res = []
#         while queue:
#             p = []
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 p.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.append(p)
#         return res[::-1]