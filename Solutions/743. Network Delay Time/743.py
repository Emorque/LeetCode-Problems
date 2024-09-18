from typing import List
import collections, heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))
        
        minHeap = [(0, k)]
        visited = set()
        time = 0

        while minHeap:
            pTime, pNode = heapq.heappop(minHeap)
            if pNode in visited:
                continue
            visited.add(pNode)
            time = pTime

            for node, nTime in adj[pNode]:
                if node not in visited:
                    heapq.heappush(minHeap, (nTime + pTime, node))
        
        return time if len(visited) == n else -1
        
