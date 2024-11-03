from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        heap = []
        for value in freq.values():
            heapq.heappush(heap, -value)
        
        cooldown = deque()
        schedule = 0
        time = 0
        while heap or cooldown:
            if heap:
                task = heapq.heappop(heap)
                if task < -1:
                    cooldown.append((task + 1, time + n))          
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])
            time += 1
            schedule += 1
        return schedule
            