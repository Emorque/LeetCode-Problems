from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice: int = prices[0]
        output: int = 0

        for price in prices:
            minPrice = min(minPrice, price)
            output = max(output, price - minPrice)
        
        return output