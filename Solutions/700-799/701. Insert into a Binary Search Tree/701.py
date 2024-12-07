from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root

        while temp:
            if val <= temp.val:
                if not temp.left:
                    temp.left = TreeNode(val)
                    return root
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = TreeNode(val)
                    return root
                else:
                    temp = temp.right
        return TreeNode(val)