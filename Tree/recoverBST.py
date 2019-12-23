# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 1
    
#     def recoverTree(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         from collections import deque
        
#         res = []
#         self.helper(root, res)
#         res.sort()
#         # print(res)
#         res = deque(res)
#         stack = []
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             root.val = res.popleft()
#             # print(root.val)
#             root = root.right
        
#     def helper(self, root, res):
#         if not root: return 
#         self.helper(root.left, res)
#         res.append(root.val)
#         self.helper(root.right, res)

    # 2 better
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res, rlist = [], []
        self.helper(root, res, rlist)
        res.sort()
        for i in range(len(res)):
            rlist[i].val = res[i]
        
    def helper(self, root, res, rlist):
        if not root: return 
        self.helper(root.left, res, rlist)
        rlist.append(root)
        res.append(root.val)
        self.helper(root.right, res, rlist)