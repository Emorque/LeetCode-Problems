from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsSort = [-num for num in nums]

        heapq.heapify(numsSort)

        for i in range(k-1):
            heapq.heappop(numsSort)
        
        return numsSort[0] * -1