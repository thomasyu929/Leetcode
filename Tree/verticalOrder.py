class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalOrder(self, root):
        from collections import deque, defaultdict
        m = defaultdict(list)
        res = []
        queue = deque([(root, 0)])
        while queue:
            node, num = queue.popleft()
            m[num].append(node)
            if node.left: queue.append((node.left, num-1))
            if node.right: queue.append((node.right, num+1))
        for i in m:
            res.append(m[i])
        return res


if __name__ == "__main__":
    
    cl = Solution()
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root.left = n2
    root.right = n3
    print(cl.verticalOrder(root))