from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves: int = 0
        def helper(root: Optional[TreeNode]) -> int:
            nonlocal moves

            if not root:
                return 0 
            left = helper(root.left)
            right = helper(root.right)

            moves += abs(left) + abs(right)

            return root.val + left + right - 1
            
        helper(root)
        return moves