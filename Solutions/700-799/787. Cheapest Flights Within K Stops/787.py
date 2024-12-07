from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n 
        costs[src] = 0
        # [0, inf, inf, inf]
        # [0, inf, inf, inf]
        # s = 0, d = 3

        for i in range(k + 1):
            clone = costs[:]
            for f, t, price in flights:
                if costs[f] == float("inf"):
                    continue
                clone[t] = min(clone[t], costs[f] + price)
            costs = clone
        
        return -1 if costs[dst] == float("inf") else costs[dst]