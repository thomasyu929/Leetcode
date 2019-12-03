# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # Recursive
    
    # def preorderTraversal(self, root):
    #     if not root:
    #         return []
    #     res = []
    #     res.append(root.val)
    #     res += self.preorderTraversal(root.left)
        
    #     res += self.preorderTraversal(root.right)
    #     return res

    # Iteration

    def preorderTraversal(self, root):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res


if __name__ == "__main__":
    
    cl = Solution()
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root.left = n2
    root.right = n3
    print(cl.preorderTraversal(root))