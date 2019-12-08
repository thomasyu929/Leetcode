# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        from collections import deque
        
        if not root:
            return []
        res = []
        queue = deque([root])
        # count = 1
        # while queue:
        #     p = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         p.append(node.val)
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #     if count % 2 == 1:
        #         res.append(p)
        #     else:
        #         res.append(p[::-1])
        #     count += 1
        # return res
    
    # optimization
        leftRight = True
        while queue:
            l = len(queue)
            p = [0]*l
            for i in range(len(queue)):
                node = queue.popleft()
                if leftRight:
                    idx = i
                else:
                    idx = l-1-i
                p[idx] = node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            leftRight = not leftRight
            res.append(p)
        
        return res       