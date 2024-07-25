from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack : List[int] = []
        # stack.append(-math.inf)
        stack.append(-2**31 - 1)

        output = True
        def helper(root: Optional[TreeNode]):
            nonlocal output
            if not root or not output:
                return
            helper(root.left)
            if root.val <= stack.pop():
                output = False
            stack.append(root.val)

            helper(root.right)
        helper(root)
        return output