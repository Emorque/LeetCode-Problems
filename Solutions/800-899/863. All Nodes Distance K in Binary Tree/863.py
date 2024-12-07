from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        nodes = {}
        output = []
        visited = []

        def helper(root, parent):
            if not root:
                return None
            nodes[root.val] = [None, None, parent]
            nodes[root.val][0] = helper(root.left, root.val)
            nodes[root.val][1] = helper(root.right, root.val)
            return root.val
        
        helper(root, None)

        def traverse(value, distance):
            if value == None or value in visited:
                return 
            if distance == 0:
                output.append(value)
            else:
                visited.append(value)
                traverse(nodes[value][0], distance-1)
                traverse(nodes[value][1], distance-1)
                traverse(nodes[value][2], distance-1)
        traverse(target.val,k)
        return output