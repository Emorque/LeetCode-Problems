from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minBanana = 1
        maxBanana = max(piles)
        
        while minBanana < maxBanana:
            midBanana = minBanana + ((maxBanana- minBanana) // 2)
            hours = 0
            for pile in piles:
                hour = pile // midBanana
                if pile % midBanana:
                    hour += 1
                hours += hour
            if hours <= h:
                maxBanana = midBanana
            else:
                minBanana = midBanana + 1
        return maxBanana