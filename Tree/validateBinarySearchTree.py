# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Recursive better
    
#     def isValidBST(self, root: TreeNode) -> bool:

#         return self.helper(root, float('-inf'), float('inf'))
#     def helper(self, root, mini, maxi):
#         if not root: return True
#         if root.val >= maxi or root.val <= mini: return False
#         return self.helper(root.left, mini, root.val) and self.helper(root.right, root.val, maxi)
    
    # recursive
    
#     def isValidBST(self, root: TreeNode) -> bool:
#         res = self.helper(root)
#         for i in range(1, len(res)):
#             if res[i-1] >= res[i]:
#                 return False
#         return True 
#     def helper(self, root):
#         res = []
#         if not root:
#             return []
#         res += self.helper(root.left)
#         res.append(root.val)
#         res += self.helper(root.right)
#         return res
       
    # stack
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        temp = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if temp >= root.val:
                return False
            else:
                temp = root.val
            root = root.right
        
        return True
            