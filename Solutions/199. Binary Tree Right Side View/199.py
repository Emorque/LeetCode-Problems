from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        nodeCount = 1
        currCount = 0

        if not root: return output

        queue = [root]

        while queue:
            for i in range(nodeCount):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    currCount += 1
                if node.right:
                    queue.append(node.right)
                    currCount += 1
            output.append(node.val)
            nodeCount = currCount
            currCount = 0

        return output