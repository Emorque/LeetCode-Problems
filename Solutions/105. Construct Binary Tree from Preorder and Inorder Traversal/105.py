from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                break

        root.left = self.buildTree(preorder[1:], inorder[:i])
        root.right = self.buildTree(preorder[1 + i:], inorder[i + 1:])

        return root