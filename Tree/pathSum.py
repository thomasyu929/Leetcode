# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 1 Recursive
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:    
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
    
    
    # 2 Stack
    
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if not root:
#             return False
#         res = []
#         stack = [(root, 0)]
        
#         while stack:
#             node, s = stack.pop()
#             if not node.left and not node.right:
#                 res.append(s + node.val)
#             if node.left:
#                 stack.append((node.left, s + node.val))
#             if node.right:
#                 stack.append((node.right, s + node.val))
                
#         return sum in res
    
    # 3 Stack       better
    
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if not root:
#             return False
#         stack = [(root, root.val)]
        
#         while stack:
#             node, s = stack.pop()
#             if not node.left and not node.right:
#                 if sum == s:
#                     return True
#             if node.left:
#                 stack.append((node.left, s + node.left.val))
#             if node.right:
#                 stack.append((node.right, s + node.right.val))
#         return False