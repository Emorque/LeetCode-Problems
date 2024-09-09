# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = 0 

        def DFS(node, maxValue):
            nonlocal output
            if node.val >= maxValue:
                output += 1
            maxValue = max(maxValue, node.val)
            if node.left:
                DFS(node.left, maxValue)
            if node.right:
                DFS(node.right, maxValue)
        
        DFS(root, root.val)
        return output