from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def LCA(root: Optional[TreeNode], startValue: int, destValue: int) -> Optional[TreeNode]:
            if not root or root.val == startValue or root.val == destValue:
                return root
            left = LCA(root.left, startValue, destValue)
            right = LCA(root.right, startValue, destValue)

            if left and right:
                return root
            return left if left else right

        def helper(root: Optional[TreeNode], destValue: int, path: list):
            if not root:
                return False
            if root.val == destValue:
                return True
            if helper(root.left, destValue, path):
                path+='L'
                return True 
            if helper(root.right, destValue, path):
                path+='R'
                return True   
            return False

        ancestor = LCA(root, startValue, destValue)
        startPath = []
        destPath = []

        helper(ancestor, startValue, startPath)
        helper(ancestor, destValue, destPath)

        startPath = 'U' * len(startPath)
        for i in range(len(destPath) - 1, -1, -1):
            startPath += destPath[i]

        return startPath