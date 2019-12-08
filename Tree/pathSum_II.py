# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # when you execute p.pop()   res.append(p) will change too 
    
    # 1 Recursive
    
#     def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
#         if not root:
#             return []   
#         res = []
#         self.helper(root, res, sum, [])
#         return res
        
#     def helper(self, root, res, s, path):
#         if not root.left and not root.right and s == root.val:
#             path.append(root.val)
#             res.append(path)
#         if root.left:
#             self.helper(root.left, res, s-root.val, path + [root.val])
#         if root.right:
#             self.helper(root.right, res, s-root.val, path + [root.val])
   


    # 2 Stack
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            node, s, path = stack.pop()
            if not node.right and not node.left and s == 0:
                res.append(path)
            if node.right:            
                stack.append((node.right, s - node.right.val, path + [node.right.val]))
            if node.left:    
                stack.append((node.left, s - node.left.val, path + [node.left.val]))

        return res