# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Recursive
        
        # if not root or root == p or root == q:
        #     return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # # if left and left != p and left != q:
        # #     return left
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if right and left: return root
        # return left if left else right
    
        # iteration
        
        stack = [root]
        parent = {root: None}
        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = []
        while p:
            ancestors.append(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q