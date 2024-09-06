# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        maxNum = max(p.val, q.val)
        minNum = min(p.val, q.val)

        while not(root.val <= maxNum and root.val >= minNum):
            if root.val > maxNum:
                root = root.left
            else:
                root = root.right
        return root