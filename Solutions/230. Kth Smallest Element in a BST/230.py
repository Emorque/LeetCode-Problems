from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = 0
        def helper(root: Optional[TreeNode]):
            nonlocal k 
            nonlocal output
            if not root or k < 0:
                return 
            helper(root.left)
            k -= 1
            if k == 0:
                output = root.val
                k -= 1
                return
            
            helper(root.right)

        helper(root)
        return output