# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    
    # Time Limit Exceeded
    
#     def rob(self, root: TreeNode) -> int:
#         if not root:
#             return 0
        
#         res = [0]
#         if root.left: res[0] += self.rob(root.left.left) + self.rob(root.left.right)
#         if root.right: res[0] += self.rob(root.right.left) + self.rob(root.right.right)
        
#         return max(root.val + res[0], self.rob(root.left) + self.rob(root.right))
            
    # Recursive
    
    def rob(self, root: TreeNode) -> int:
        m = {}
        return self.robMap(root, m)
    def robMap(self, root, m):
        if not root:
            return 0
        if root in m:
            return m[root]
        res = [0]
        if root.left: res[0] += (self.robMap(root.left.left, m) + 
            self.robMap(root.left.right, m))
        if root.right: res[0] += (self.robMap(root.right.left, m) + 
            self.robMap(root.right.right, m))
        
        res[0] = max(res[0] + root.val, self.robMap(root.left, m) + 
                      self.robMap(root.right, m))
        m[root] = res[0]
        return res[0]

    # recursive

    need to understand

    def rob(self, root: TreeNode) -> int:
        res = self.helper(root)
        return max(res)
    def helper(self, root):
        if not root:
            return [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = left[0] + right[0] + root.val
        return res