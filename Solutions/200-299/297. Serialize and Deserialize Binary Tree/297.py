# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"

        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return str(root.val) + "," + left + "," + right
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        serial = data.split(',')
        self.index = 0

        def dfs():
            if serial[self.index] == "null":
                self.index += 1
                return None
            root = TreeNode(serial[self.index])
            self.index += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))