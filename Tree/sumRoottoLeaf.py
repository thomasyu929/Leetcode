 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 1 Recursive   
    
#     def sumNumbers(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         s = []
#         self.helper(root, 0, s)
#         return sum(s)
    
#     def helper(self, root, n, s):       
#         # notice s can't be plus because s in left and right are separate calculate 
#         if not root.left and not root.right:
#             s.append(n*10 + root.val)
#         if root.left:
#             self.helper(root.left, n*10 + root.val, s)
#         if root.right:
#             self.helper(root.right, n*10 + root.val, s)
    
    # 2 stack
    
    def sumNumbers(self, root):
        if not root:
            return 0
        res = 0
        stack = [(root, 0)]
        while stack:
            node, n = stack.pop()
            if not node.left and not node.right:
                res += (n*10 + node.val)
            if node.left:
                stack.append((node.left, n*10 + node.val))
            if node.right:
                stack.append((node.right, n*10 + node.val))
        return res