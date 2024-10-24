from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node1, node2) -> bool: 
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (not node2 and node1):
                return False
            return node1.val == node2.val and sameTree(node1.left, node2.left) and sameTree(node1.right, node2.right)
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val and sameTree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False