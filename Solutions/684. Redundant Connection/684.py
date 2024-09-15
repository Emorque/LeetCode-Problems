from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents, size = [], []

        for i in range(len(edges) + 1):
            parents.append(i)
            size.append(1)
        
        def getParent(n):
            p = parents[n]
            while p != parents[p]:
                p = parents[p]
            return p
        
        def setParents(n1, n2):
            p1, p2 = getParent(n1), getParent(n2)

            if p1 == p2:
                return False
            
            size1, size2 = size[p1], size[p2]

            if size1 > size2:
                parents[p2] = parents[p1]
                size[p2] += size[p1]
            else:
                parents[p1] = parents[p2]
                size[p1] += size[p2]

            return True
        
        for a, b in edges:
            if not setParents(a, b):
                return [a,b]
                