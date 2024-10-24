from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone = (heapq.heappop(heap) * -1) - (heapq.heappop(heap) * -1)
            if stone != 0:
                heapq.heappush(heap, -stone)
            
        return -heap[0] if len(heap) == 1 else 0