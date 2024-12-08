from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            nonlocal maxSum
            currSum = node.val

            left = dfs(node.left)
            right = dfs(node.right)

            if left > 0:
                currSum += left

            if right > 0:
                currSum += right

            maxSum = max(maxSum, currSum)
            return max(node.val, node.val + left, node.val + right)
        dfs(root)
        return maxSum