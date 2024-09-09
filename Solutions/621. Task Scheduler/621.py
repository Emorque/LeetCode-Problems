from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        charFreq = {}
        charSeen = []
        chars = []
        output = 0

        for task in tasks:
            charFreq[task] = 1 + charFreq.get(task, 0)

        for key, value in charFreq.items():
            heapq.heappush(chars, (value * -1, key))
        
        interval = 0
        while chars or charSeen:
            if not chars:
                while charSeen:
                    heapq.heappush(chars, charSeen.pop())
                output += n + 1
                interval = 0
            freq = heapq.heappop(chars)
            if freq[0] != -1:
                charSeen.append((freq[0] + 1, freq[1]))
            interval += 1
            if interval == n + 1:
                while charSeen:
                    heapq.heappush(chars, charSeen.pop())
                output += interval
                interval = 0
                
        return output + interval