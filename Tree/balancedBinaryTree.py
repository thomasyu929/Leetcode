# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    '''
    Empty tree is also a Balanced binary tree
    '''
    
    # 1 Recursive
    
#     def isBalanced(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         if abs(self.helper(root.left) - self.helper(root.right)) > 1:
#             return False
#         return self.isBalanced(root.left) and self.isBalanced(root.right)
    
#     def helper(self, root):
#         if not root:
#             return 0
#         return 1 + max(self.helper(root.left), self.helper(root.right))
    
    # 2 Recursive better
    
    def isBalanced(self, root: TreeNode) -> bool:
        if self.helper(root) == -1: return False
        return True
    
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == -1: return -1
        if right == -1: return -1
        if abs(left - right) > 1: return -1
        return 1 + max(left, right)
    