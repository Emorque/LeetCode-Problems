from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        original = [float("inf")] * n   
        original[src] = 0

        while k != -1:
            copy = original.copy()
            for fro, to, price in flights:
                if copy[fro] + price < original[to]:
                    original[to] = copy[fro] + price
            k -= 1
        
        return original[dst] if original[dst] != float("inf") else -1