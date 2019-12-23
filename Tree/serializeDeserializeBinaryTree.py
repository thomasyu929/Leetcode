# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

    # Recursive

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        res = []
        self.helperSeri(root, res)
        return str(res)

    def helperSeri(self, root, res):
        if not root: return res.append(None)
        res.append(root.val)
        self.helperSeri(root.left, res)
        self.helperSeri(root.right, res)

        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "": return None
        data = data[1:-1].split(',')
        i = [0]
        return self.helperDeseri(data, i)
    
    def helperDeseri(self, data, i):
        if data[i[0]] == ' None':
            i[0] += 1
            return None
        root = TreeNode(int(data[i[0]]))
        i[0] += 1
        root.left = self.helperDeseri(data, i)
        root.right = self.helperDeseri(data, i)
        return root


    # Iteration

# from collections import deque

# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """

#         data = ""
#         queue = deque([root])
#         while queue:
#             node = queue.popleft()
#             if not node:
#                 data += ",null"
#                 continue
#             else:
#                 data += ',' + str(node.val)
#                 queue.append(node.left)
#                 queue.append(node.right)
#         return '[' + data[1:] + ']'

        
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         data = deque(data[1:-1].split(','))
#         val = data.popleft()
#         root = None if val == 'null' else TreeNode(int(val))
#         queue = deque([root])
#         while queue:
#             node = queue.popleft()
#             if not node: continue
#             left, right = data.popleft(), data.popleft()
#             node.left = None if left == 'null' else TreeNode(int(left))
#             node.right = None if right == 'null' else TreeNode(int(right))
#             queue.append(node.left)
#             queue.append(node.right)
#         return root
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))