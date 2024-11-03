from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        queue = deque()

        if root:
            queue.append((root, root.val))
        
        while queue:
            node, greatest_val = queue.popleft()
            if node.val >= greatest_val:
                good += 1
            if node.left:
                queue.append((node.left, max(node.val, greatest_val)))
            if node.right:
                queue.append((node.right, max(node.val, greatest_val)))
        return good