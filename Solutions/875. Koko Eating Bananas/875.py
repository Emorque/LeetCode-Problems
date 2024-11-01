from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        k = 1

        while low <= high:
            mid = low + (high - low) // 2
            time = 0
            for pile in piles:
                time += pile // mid
                if pile % mid != 0:
                    time += 1
            
            if time <= h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1
        return k