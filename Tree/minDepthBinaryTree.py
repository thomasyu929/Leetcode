# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return 1 + self.minDepth(root.right)
        if not root.right: return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    
    
    # 1 Recursive
    
#     def minDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         res = []
#         self.helper(root, 1, res)
#         return min(res)
        
        
#     def helper(self, root, count, res):
#         if not root.right and not root.left:
#             res.append(count)
#         if root.left:
#             self.helper(root.left, count+1, res)
#         if root.right:
#             self.helper(root.right, count+1, res)
            
    # 2 Stack
    
#     def minDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         res = []
#         stack = [(root, 1)]
#         while stack:
#             node, count = stack.pop()
#             if not node.left and not node.right:
#                 res.append(count)
#             if node.left:
#                 stack.append((node.left, count + 1))
#             if node.right:
#                 stack.append((node.right, count + 1))
#         return min(res)
        