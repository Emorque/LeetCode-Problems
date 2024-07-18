from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        nodePaths: list[int] = []
        def getNodePaths(root: TreeNode, currPath: list[TreeNode]):
            currPath = currPath + [root]
            if not root.left and not root.right:
                nodePaths.append(currPath)
                return
            if root.left:
                getNodePaths(root.left, currPath)
            if root.right:
                getNodePaths(root.right, currPath) 

        output = 0
        getNodePaths(root, [])

        for i in range(len(nodePaths) - 1):
            j = i + 1
            currPath = nodePaths[i]
            while j < len(nodePaths):
                comparePath = nodePaths[j]
                currDistance = 0
                p1 = len(currPath) - 1
                p2 = len(comparePath) -1
                while p1 != 0 and p2 != 0:
                    if p1 > p2:
                        p1 -= 1
                        currDistance += 1
                        continue
                    if p2 > p1:
                        p2 -= 1
                        currDistance += 1
                        continue
                    if currPath[p1] == comparePath[p2]:
                        break 
                    if p1 != 0:
                        p1 -= 1
                        currDistance += 1
                    if p2 != 0:
                        p2 -= 1
                        currDistance += 1    
                    if currDistance > distance:
                        break
                if currDistance > distance:
                    j += 1
                    continue
                else:
                    output += 1
                    j+= 1
        return output