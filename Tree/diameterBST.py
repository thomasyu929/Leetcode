# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         h = [0]
#         self.helper(root, h)
#         return h[0]
        
#     def helper(self, root, h):
#         if not root: return 0
#         left = self.helper(root.left, h)
#         right = self.helper(root.right, h)
#         h[0] = max(h[0], left + right)
#         return max(left, right) + 1

    # use self.res

#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         self.res = 0
#         self.helper(root, self.res)
#         return self.res
        
#     def helper(self, root, res):
#         if not root: return 0
#         left = self.helper(root.left, self.res)
#         right = self.helper(root.right, self.res)
#         self.res = max(self.res, left + right)
#         return max(left, right) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        stack = [(1, root)]
        d = {None: -1}
        diameter = 0
        while stack:
            indicator, node = stack.pop()
            if node is None:
                continue
            if indicator:
                # doing post-order traversal here
                stack.extend([(0, node), (1, node.right), (1, node.left)])
            else:
                left = d[node.left] + 1
                right = d[node.right] + 1
                d[node] = max(left, right)
                # build the hashtable from bottom up
                # the key is the node, the value is the node's max depth
                diameter = max(diameter, left + right)
        return diameter

        
        