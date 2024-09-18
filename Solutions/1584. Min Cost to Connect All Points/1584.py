from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        numPoints = len(points)

        adj = { i:[] for i in range(numPoints)} #Initializes each point(index) with an empty adjacent list 
        
        for i in range(numPoints):
            x1, y1 = points[i]
            for j in range(i + 1, numPoints):
                x2, y2 = points[j]
                manhattan = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([manhattan, j])
                adj[j].append([manhattan, i])


        output = 0
        visited = set()
        heap = [[0,0]]
        while len(visited) < numPoints:
            cost, point = heapq.heappop(heap)
            if point in visited:
                continue
            output += cost
            visited.add(point)

            for aCost, aPoint in adj[point]:
                if aPoint not in visited:
                    heapq.heappush(heap, [aCost, aPoint])
        
        return output