# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Recursive
    
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if not root:
#             return []
#         res += self.inorderTraversal(root.left)
#         res.append(root.val)
#         res += self.inorderTraversal(root.right)
#         return res
    
    # Stack
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = [] 
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
            
        return res