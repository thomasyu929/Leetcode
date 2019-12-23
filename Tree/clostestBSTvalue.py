class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # recursive

    # def clostestBSTvalue(self, root, target):
    #     res = []
    #     x = float('inf')
    #     self.helper(root, res)
    #     for i in res:
    #         if x > abs(target - i):
    #             temp = i
    #             x = abs(target - i)
    #     return int(temp)
        
    # def helper(self, root, res):
    #     if not root: return
    #     self.helper(root.left, res)
    #     res.append(float(root.val))
    #     self.helper(root.right, res)

    # iteration

    # def clostestBSTvalue(self, root, target):
    #     res = root.val
    #     while root:
    #         if abs(res - target) >= abs(root.val - target):
    #             res = root.val
    #         root = root.left if target < root.val else root.right
    #     return res

    # recursive

    def clostestBSTvalue(self, root, target):
        res = root.val
        if (target < root.val) and root.left:
            l = self.clostestBSTvalue(root.left, target)
            if abs(res - target) > abs(l - target): res = l
        elif (target > root.val) and root.right:
            r = self.clostestBSTvalue(root.right, target)
            if abs(res - target) > abs(r - target): res = r
        return res


if __name__ == "__main__":
    
    cl = Solution()
    root = TreeNode(2)
    n2 = TreeNode(1)
    n3 = TreeNode(3)
    root.left = n2
    root.right = n3
    target = 1.3
    print(cl.clostestBSTvalue(root, target))