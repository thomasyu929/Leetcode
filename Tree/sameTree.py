# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # Recursive
        
        # if not p or not q:
        #     return p == q
        # return p.val == q.val and self.isSameTree(p.left, q.left) and         self.isSameTree(p.right, q.right)

        # Stack

        stack = [(p, q)]
        while stack:
            nodeP, nodeQ = stack.pop()
            if not nodeP and not nodeQ:
                continue
            elif None in [nodeP, nodeQ]:
                return False
            else:
                if nodeP.val != nodeQ.val:
                    return False
                stack.append((nodeP.right, nodeQ.right))
                stack.append((nodeP.left, nodeQ.left))
        return True