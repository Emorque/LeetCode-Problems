from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        def dfs(node: Optional[TreeNode], dep: int):
            if not node:
                return
            if dep == depth-1:
                tempLeft = node.left
                tempRight = node.right
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = tempLeft
                node.right.right = tempRight
            else:
                dfs(node.left, dep+1)
                dfs(node.right, dep+1)
        dfs(root, 1)
        return root
        