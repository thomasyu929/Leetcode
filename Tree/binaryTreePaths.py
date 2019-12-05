# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 1 Recursive 
    
#     def binaryTreePaths(self, root: TreeNode) -> List[str]:
#         res = []
#         self.helper(root, [], res)
        
#         return res
    
#     def helper(self, root, path, res):
#         if root:
#             path.append(str(root.val))
#             left = self.helper(root.left, path, res)
#             right = self.helper(root.right, path, res)
#             if not left and not right:
#                 res.append('->'.join(path))
#             path.pop()
#             return True
        
    # 2 Recursive
    
#     def binaryTreePaths(self, root):
#         if not root:
#             return []
#         res = []
#         self.helper(root, "", res)
        
#         return res
    
#     def helper(self, root, path, res):
#         if not root.left and not root.right:
#             res.append(path + str(root.val))
#         if root.left:
#             self.helper(root.left, path + str(root.val) + '->', res)
#         if root.right:
#             self.helper(root.right, path + str(root.val) + '->', res)

    # 3 Stack
    
#     def binaryTreePaths(self, root):
#         if not root:
#             return []
#         stack = [(root, "")]
#         res = []
#         while stack:
#             node, path = stack.pop()
#             if not node.left and not node.right:
#                 res.append(path + str(node.val))
#             if node.left:
#                 stack.append((node.left, path + str(node.val) + '->'))
#             if node.right:
#                 stack.append((node.right, path + str(node.val) + '->'))
#         return res
    
    # 4 Queue
    
    def binaryTreePaths(self, root):
        
        from collections import deque
        
        if not root:
            return []
        res = []
        queue = deque([(root, "")])
        
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                res.append(path + str(node.val))
            if node.left:
                queue.append((node.left, path + str(node.val) + '->'))
            if node.right:
                queue.append((node.right, path + str(node.val) + '->'))
        return res
        