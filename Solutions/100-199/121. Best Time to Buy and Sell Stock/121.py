from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            profit = price - minPrice
            if profit > maxProfit:
                maxProfit = profit
            if price < minPrice:
                minPrice = price
        return maxProfit