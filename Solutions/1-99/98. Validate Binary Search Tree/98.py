from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, leftRange, rightRange) -> bool:
            if not node:
                return True 
            if not(leftRange < node.val < rightRange):
                return False
            return helper(node.left, leftRange, node.val) and helper(node.right, node.val, rightRange)
        return helper(root, float('-inf'), float('inf'))