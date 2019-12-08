# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
determine the maximum path of the child node, store to res
store max(left, right) as max path in high level 
'''


class Solution:

    # recursive     DFS + BackTracking
    
    def maxPathSum(self, root: TreeNode) -> int:
        res = [float('-inf')]
        self.helper(root, res)
        return res[0]
    
    def helper(self, root, res):
        if not root:
            return 0
        left = max(self.helper(root.left, res), 0)
        right = max(self.helper(root.right, res), 0)
        res[0] = max(res[0], left + right + root.val)
        return max(left, right) + root.val
