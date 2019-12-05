# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 1 Recursive
    
#     def isSymmetric(self, root: TreeNode) -> bool:
        
#         if not root:
#             return True
#         return self.isLRSymmetric(root.left, root.right)
    
#     def isLRSymmetric(self, left, right):
        
#         if not left and not right:
#             return True
        
#         if (not left and right) or (left and not right) or (left.val != right.val):
#             return False
#         return self.isLRSymmetric(left.left, right.right) and self.isLRSymmetric(left.right, right.left)
    
    # 2 Iteration
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        queue1, queue2 = [root.left], [root.right]
        
        while queue1 and queue2:
            node1, node2 = queue1.pop(), queue2.pop()
            if not node1 and not node2:
                continue
            if (not node1 and node2) or (node1 and not node2):
                return False
            if node1.val != node2.val:
                return False
            
            queue1.append(node1.left)
            queue1.append(node1.right)
        
            queue2.append(node2.right)
            queue2.append(node2.left)
        return True