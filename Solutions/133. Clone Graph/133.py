# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}

        def dfs(root):
            if root in hashmap:
                return hashmap[root]
            if not root:
                return 
            clone = Node(root.val)
            hashmap[root] = clone

            for neighbor in root.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        
        return dfs(node)