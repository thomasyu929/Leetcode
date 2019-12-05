# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Recursive
    
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return 
#         root.left, root.right = root.right, root.left
#         self.invertTree(root.left)
#         self.invertTree(root.right)
        
#         return root
    
    # Iteration
    
    def invertTree(self, root):
        if not root:
            return
        queue = [root]
        
        while queue:
            node = queue.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            # if node:
            #     node.left, node.right = node.right, node.left
            #     stack += node.left, node.right
            
            
        return root