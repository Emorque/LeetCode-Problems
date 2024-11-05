from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n 
        prices[src] = 0


        for i in range(k + 1):
            temp_prices = prices[:]
            for f, t, p in flights:
                if prices[f] == float('inf'):
                    continue
                if prices[f] + p < temp_prices[t]:
                    temp_prices[t] =  prices[f] + p
                
            prices = temp_prices
        cost = prices[dst]
        return cost if cost != float('inf') else -1