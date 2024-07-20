from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output: List[List[int]] = []
        queue = []

        if not root:
            return output

        queue.append(root)

        while len(queue) != 0:
            currLevel = []
            for i in range(len(queue)):
                currNode = queue.pop(0)

                currLevel.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            output.append(currLevel)
        return output