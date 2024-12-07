from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = [None, None]
            if isLeft == 1:
                nodes[parent][0] = child
            else:
                nodes[parent][1] = child
            children.add(child)
        
        for parent in nodes.keys():
            if parent not in children:
                rootVal = parent

        def helper(value: int):
            if value == None:
                return
            root = TreeNode(value)
            
            if value in nodes.keys():
                root.left = helper(nodes[value][0])
                root.right = helper(nodes[value][1])
            
            return root

        root = helper(rootVal)
        return root