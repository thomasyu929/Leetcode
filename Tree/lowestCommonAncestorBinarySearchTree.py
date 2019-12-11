# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#   ancestor 和 p ， q 比较  要么都大   要么都小    除此之外 返回root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        return root        
        
        # iteration
        
        # while root:
        #     if min(p.val, q.val) > root.val:
        #         root = root.right
        #     elif max(p.val, q.val) < root.val:
        #         root = root.left
        #     else:
        #         return root
        # return None
         