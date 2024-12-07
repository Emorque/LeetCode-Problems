from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        size = [1] * n

        #find
        def find(node):
            p = parents[node]
            while p != parents[p]:
                p = parents[p]
            return p
        
        #union
        for a, b in edges:
            parA, parB = find(a), find(b)
            if parA == parB:
                continue
            
            n-= 1

            if size[parA] > size[parB]:
                parents[parB] = parA
                size[parA] += size[parB]
            else:
                parents[parA] = parB
                size[parB] += size[parA]
        return n