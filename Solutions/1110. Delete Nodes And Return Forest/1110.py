from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        output: List[TreeNode] = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root.val in to_delete:
                if root.left:
                    output.append(root.left)
                if root.right:
                    output.append(root.right)
                return None
            else:
                return root
            return root
                
        if dfs(root):
            output.append(root)
            
        return output