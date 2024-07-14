from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(currNode: Optional[TreeNode]) -> int:
            if not currNode:
                return 0
            
            leftHeight = helper(currNode.left)
            rightHeight= helper(currNode.right)

            if (leftHeight == -1 or rightHeight == -1):
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            return max(leftHeight + 1, rightHeight + 1)
        result = helper(root)
        return result >= 0