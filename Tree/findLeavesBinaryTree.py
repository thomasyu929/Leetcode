class Treeroot:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:

    def findLeaves(self, root: Treeroot):
        res = []
        while root:
            leaves = []
            root = self.helper(root, leaves)
            res.append(leaves)
        return res
    
    def helper(self, root, leaves):
        if not root:
            return 
        if not root.left and not root.right:
            leaves.append(root.val)
            return None
        root.left = self.helper(root.left, leaves)
        root.right = self.helper(root.right, leaves)

        return root



if __name__ == "__main__":
    
    cl = Solution()
    root = Treeroot(1)
    n2 = Treeroot(2)
    n3 = Treeroot(3)
    n4 = Treeroot(4)
    n5 = Treeroot(5)
    # n6 = Treeroot(2)
    # n7 = Treeroot(2)
    # n8 = Treeroot(4)
    # n9 = Treeroot(3)
    root.left = n2
    root.right = n3
    n2.left = n4
    n2.right = n5
    # n3.left = n6
    # n3.right = n7
    # n4.left = n8
    # n4.right = n9
    print(cl.findLeaves(root))
            