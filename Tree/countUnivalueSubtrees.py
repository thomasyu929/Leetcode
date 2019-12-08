class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:

    def countUnivalueSubtrees(self, root: TreeNode):
        m = {}
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        res = res[1:]
        for i in res:
            m[i] = m.get(i, 0) + 1
        return max(m.values())
        
if __name__ == "__main__":
    
    cl = Solution()
    root = TreeNode(2)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(3)
    n5 = TreeNode(2)
    n6 = TreeNode(2)
    n7 = TreeNode(2)
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
    print(cl.countUnivalueSubtrees(root))