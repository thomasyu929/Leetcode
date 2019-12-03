# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        from collections import deque
        
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            p = []
            for _ in range(len(queue)):
                node = queue.popleft()
                p.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(p)
        return res