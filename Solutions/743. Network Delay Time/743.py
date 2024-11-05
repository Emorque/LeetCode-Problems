from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[] for i in range(n + 1)]
        for u, v, w in times:
            edges[u].append((v, w)) 
        
        visited = set()
        time = 0

        minHeap = [(0, k)]

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)

            time = weight

            for target, w in edges[node]:
                if target not in visited:
                    heapq.heappush(minHeap, (weight + w, target))
            
        return time if len(visited) == n else -1