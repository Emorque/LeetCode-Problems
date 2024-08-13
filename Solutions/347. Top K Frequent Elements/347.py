from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        occurances = []
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1

        for key, v in hashmap.items():
            occurances.append((-v,key))
        heapq.heapify(occurances)
        output = []
        while k != 0:
            output.append(heapq.heappop(occurances)[1])
            k-= 1
        return output
        