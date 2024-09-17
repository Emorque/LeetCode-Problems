from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = {}

        def dfs(day, buying):
            if day >= len(prices):
                return 0
            if (day, buying) in profits:
                return profits[(day, buying)]
            
            if buying:
                buy = dfs(day + 1, False) - prices[day]
                cooldown = dfs(day + 1, True)
                profits[(day,buying)] = max(buy, cooldown)
            else:
                sell = dfs(day + 2, True) + prices[day]
                cooldown = dfs(day + 1, False)
                profits[(day, buying)] = max(sell, cooldown)
            return profits[(day, buying)]
        
        return dfs(0, True)