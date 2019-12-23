class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # iteration

    # def inorderSuccessorBST(self, root, p):
    #     stack = []
    #     b = False
    #     while stack or root:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         root = stack.pop()
    #         if b == True: return root.val
    #         if root == p: b = True
    #         root = root.right
    #     return None



    # def inorderSuccessorBST(self, root, p):
    #     while root:
    #         if root.val > p.val:
    #             res = root
    #             root = root.left
    #         else:
    #             root = root.right
    #         # else:
    #         #     if root.right:
    #         #         return root.right.val
    #         #     else:
    #         #         return None
    #     return res
    
    # Recursive

    def inorderSuccessorBST(self, root, p):
        if not root: return None
        if root.val <= p.val:
            return self.inorderSuccessorBST(root.right, p)
        else:
            left = self.inorderSuccessorBST(root.left, p)
            return left if left else root



if __name__ == "__main__":
    
    cl = Solution()
    root = p = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root.left = n2
    root.right = n3
    print(cl.inorderSuccessorBST(root, p))

            