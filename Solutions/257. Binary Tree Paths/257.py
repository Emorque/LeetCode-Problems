from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result : List[str] = []
        if not root:
            return result

        def helper(currNode: Optional[TreeNode], currStr: str):
            if not currNode.left and not currNode.right:
                result.append(currStr+str(currNode.val))
            currStr += str(currNode.val)+"->"
            if currNode.left:
                helper(currNode.left, currStr)
            if currNode.right:
                helper(currNode.right, currStr)

        helper(root, "")
        return result