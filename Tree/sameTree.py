# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # Recursive
        
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        # Stack 1   use preorder travelsal
        
        if not p or not q:
            return p == q
        res1, res2 = [], []
        stack1, stack2 = [p], [q]
        while stack1 or stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if not node1 and node2:
                continue
            res1.append(node1.val)
            res2.append(node2.val)
            stack1.append(node1.right)
            stack1.append(node1.left)
            stack2.append(node2.right)
            stack2.append(node2.left)
        return res1 == res2
    
        # Stack 2      whick is better

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
                 