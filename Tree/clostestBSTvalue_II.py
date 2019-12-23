# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def closestKvalues(self, root, target, k):
        nums = []
        self.helper(root, nums)
        res = []
        m = {}
        for i in nums:
            m[abs(target - i)] = i
        while k > 0:
            res.append(m[min(m.keys())])
            m.pop(min(m.keys()))
            k -= 1
        return res


    def helper(self, root, nums):
        if not root: return
        self.helper(root.left, nums)
        nums.append(root.val)
        self.helper(root.right, nums)


if __name__ == "__main__":
    
    cl = Solution()
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    root.left = n2
    root.right = n3
    target = 2.1
    k = 2
    print(cl.closestKvalues(root, target, k))   