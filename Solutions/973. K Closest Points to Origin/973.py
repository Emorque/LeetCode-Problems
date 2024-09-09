from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        output = [0] * k

        for x,y in points:
            distance = sqrt(x ** 2 + y ** 2)                
            heapq.heappush(heap, (distance, (x,y)))

        for i in range(k):
            output[i] = heapq.heappop(heap)[1]
            
        return output