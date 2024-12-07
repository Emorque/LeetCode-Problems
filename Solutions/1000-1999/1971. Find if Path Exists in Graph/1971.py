from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True

        vertexes = {}
        for u, v in edges:
            if u not in vertexes:
                vertexes[u] = [v]
            else:
                vertexes[u].append(v)
            if v not in vertexes:
                vertexes[v] = [u]
            else:
                vertexes[v].append(u)

        visited = set()

        def helper(vertex: int):
            if vertex in visited or destination in visited:
                return
            visited.add(vertex)
            for dest in vertexes[vertex]:
                helper(dest)
                
        helper(source)
        return destination in visited