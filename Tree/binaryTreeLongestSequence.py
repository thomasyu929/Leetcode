'''
Given a binary tree, 
find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to 
any node in the tree along the parent-child connections. 
The longest consecutive path need to be from parent to child 
(cannot be the reverse).
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 1 Stack

    def longestSequence(self, root):
        if not root:
            return 0
        res = [0]
        stack = [(root, root.val, 0, res)]
        while stack:
            node, v, count, res= stack.pop()
            if not node:
                continue
            if node.val - v == 1:
                count += 1
            else:
                count = 1
            res[0] = max(res[0], count)
            if node.right:
                stack.append((node.right, node.val, count, res))
            if node.left:
                stack.append((node.left, node.val, count, res))
        return res[0]

    # 2 Recursive

    # def longestSequence(self, root):
    #     if not root:
    #         return 0
    #     res = [0]
    #     self.helper(root, root.val, 0, res)
    #     return res[0]
    
    # def helper(self, root, value, count, res):
    #     if not root:
    #         return
    #     if root.val == value + 1:
    #         count += 1
    #     else:
    #         count = 1
    #     res[0] = max(res[0], count)
    #     self.helper(root.left, root.val, count, res)
    #     self.helper(root.right, root.val, count, res)

if __name__ == "__main__":
    
    cl = Solution()
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(3)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(4)
    n8 = TreeNode(4)
    n9 = TreeNode(3)
    root.left = n2
    root.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9
    print(cl.longestSequence(root))
