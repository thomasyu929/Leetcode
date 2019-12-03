# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Recursive
    
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if not root:
#             return []
#         res += self.postorderTraversal(root.left)
#         res += self.postorderTraversal(root.right)
#         res.append(root.val)
        
#         return res
    
    # Stack
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]