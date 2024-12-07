import heapq
from typing import List
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, ((sqrt(x**2 + y**2), (x, y))))
        
        closest_points = []
        for i in range(k):
            closest_points.append(heapq.heappop(heap)[1])
        return closest_points